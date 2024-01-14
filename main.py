#importing files and libraries
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow -> this is only to be used when using google colab!
from matplotlib import pyplot as plt
from tensorflow import Keras

#frame - has 240x320 pixels in our current example
#pixel - (0-255,0-255,0-255)
#we receive the frame already in a shape of (240,320,3)
#we need to flatten it in order to put it in a model my_instance.reshape(amount_of_frames, 240*320*3)


# the following code is how we capture a video using cv2 library

cap = cv2.VideoCapture("Abuse001_x264.mp4")
while True:

    ret, frame = cap.read()
    if ret is False:
        break
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # if pressed on escape
        break

cap.release()
cv2.destroyAllWindows()

label = [0, 1]  # normal / anomaly
