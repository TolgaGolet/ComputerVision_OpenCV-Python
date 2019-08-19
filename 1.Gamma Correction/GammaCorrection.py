import cv2
import numpy as np

inputImage = cv2.imread('balloon.jpg', 0)

gamma = 2

lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
res = cv2.LUT(inputImage, lookUpTable)

cv2.imshow('Original', inputImage)
cv2.imshow('gamma', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
