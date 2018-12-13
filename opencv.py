import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret,frame =camera.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_colour = np.array([0,69,100])
    higher_colour = np.array([80,165,255])

    mask = cv2.inRange(hsv,lower_colour, higher_colour)
    cv2.imshow("Masked", mask)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.distroyallwindows()
