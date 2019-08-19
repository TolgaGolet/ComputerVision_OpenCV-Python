import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('balloon.png',0)
print(np.mean(img))    #ortalama değer
ret,thresh1 = cv.threshold(img,100,255,cv.THRESH_BINARY)   #soldaki sayılar threshold
ret,thresh2 = cv.threshold(img,95,255,cv.THRESH_BINARY)
ret,thresh3 = cv.threshold(img,90,255,cv.THRESH_BINARY)
ret,thresh4 = cv.threshold(img,105,255,cv.THRESH_BINARY)
ret,thresh5 = cv.threshold(img,110,255,cv.THRESH_BINARY)
hist = plt.hist(img.ravel(),256,[0,256]); plt.show()
titles = ['Original Image', 'BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']   #eski başlıklar
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
