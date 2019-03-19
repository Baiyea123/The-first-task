# import all the package we need
from imutils.video import FPS
import numpy as np
import cv2
import imutils

# create video object, start FPS timer and initialize frame number
cap = cv2.VideoCapture('test.mp4')
fps = FPS().start()
num = 0

# loop to display the video
while True:
    # read frame, break while no next frame exist
    (ret, frame) = cap.read()
    if not ret:
        break

    # change to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display frame and update character value
    cv2.imshow('frame', gray)
    num = num + 1
    fps.update()

    # if press 'q', break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# stop fps timer
fps.stop()

# display video character information
print("time length: {:.2f}".format(fps.elapsed()))
print("frame rate: {:.2f}".format(fps.fps()))
print("frame number: {:d}".format(num))

# release video object and close all windows
cap.release()
cv2.destroyAllWindows()
