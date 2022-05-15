import cv2
from PIL import Image
import os
import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate', 130)
videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()

os.system('python3 detectnet.py NewPicture.jpg Output.jpg')


infile = "read.text"
f = open(infile, 'r')
theText = f.read()
f.close()
engine.say(theText)
engine.runAndWait()

