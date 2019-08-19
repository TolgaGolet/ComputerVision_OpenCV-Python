import cv2
import numpy as np

inputImage = cv2.imread('balloon.jpg')

img2 = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original', inputImage)
cv2.imshow('Grayscale', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
