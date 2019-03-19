import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        # frame = cv2.flip(frame, 0)

        # break the image into its RGB components, then construct the
        # RGB representation of each frame individually
        (B, G, R) = cv2.split(frame)
        gray = cv2.merge([G, G, G])

        # write the flipped frame
        out.write(gray)

        cv2.imshow('Gray', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
