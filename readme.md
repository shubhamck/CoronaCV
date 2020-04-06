# Description
During this time of a major pandemic, many software engineers are forced to work from home. While working from home, it is also essential to take care of yourself, especially following simple rules like *avoiding touching your mouth or nose*. But we are humans and we tend to not follow this rule unintentionally.

To help with this, I created this app which runs in the background, using your laptop webcam and analyzing your face. If you try to touch your face, it will notify you. Currently the notification is text based in terminal, but I am working on it to make it audio based or in the form of desktop notification.

## How to run
* `git clone https://github.com/shubhamck/CoronaCV`
* `cd CoronaCV`
* `python face_detector.p`

## Prerequisites
* OpenCV for Python `pip install opencv-python`
* [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)
* [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
* [haarcascade_nose.xml](https://github.com/sightmachine/SimpleCV/blob/master/SimpleCV/Features/HaarCascades/nose.xml)
* [haarcascade_mouth.xml](https://github.com/sightmachine/SimpleCV/blob/master/SimpleCV/Features/HaarCascades/mouth.xml)
* Make a directory `mkdir models`
* `cd models`
* Download the above trained models for eye, face, noise and mouth and store them in the files with same names and extension in `models` directory
