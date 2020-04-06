import numpy as np
import cv2
from playsound import playsound
import threading
c = threading.Condition()
# Detectors
face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("models/haarcascade_eye.xml")
nose_cascade = cv2.CascadeClassifier("models/haarcascade_nose.xml")
mouth_cascade = cv2.CascadeClassifier("models/haarcascade_mouth.xml")

# global vars
ALERT_USER = False

# Thresholds
FACE_BOX_AREA_THRESHOLD = 40000

class AudioThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global ALERT_USER
        while (True):
            c.acquire()
            if (ALERT_USER):
                print "Please dont touch your face"
                # playsound('do_not_touch_your_face.mp3')
            c.release()


class VideoThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        cap = cv2.VideoCapture(0)
        global ALERT_USER

        while(True):
            # read image
            c.acquire()
            ret, img = cap.read()
            # convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            ALERT_USER = False

            faces = face_cascade.detectMultiScale(gray, 1.03, 1)
            print "faces : ", len(faces)
            for (x,y,w,h) in faces:
                if (w * h < FACE_BOX_AREA_THRESHOLD):
                    continue
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 10)
                nose = nose_cascade.detectMultiScale(roi_gray, 1.3, 10)
                mouth = mouth_cascade.detectMultiScale(roi_gray, 1.3, 100)
                print "eyes : ", len(eyes)
                print "nose : ", len(nose)
                print "mouth : ", len(mouth)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
                for (nx,ny,nw,nh) in nose:
                    cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(0,255,0),2)
                for (mx,my,mw,mh) in mouth:
                    cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(255,255,0),2)

                if (len(mouth) < 1):
                    ALERT_USER = True
                    c.notify_all()
                # else:
                #     c.wait()
            c.release()

            cv2.imshow('img',img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()

# When everything done, release the capture
if __name__ == "__main__":
    a = VideoThread("myThread_name_A")
    b = AudioThread("myThread_name_B")

    b.start()
    a.start()

    a.join()
    b.join()

    # both threads completely executed
    print("Done!")
