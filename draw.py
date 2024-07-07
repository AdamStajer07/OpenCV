import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

cv.rectangle(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

cv.line(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Line', blank)

cv.putText(blank, 'Js is better than Py', (0,blank.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0))
cv.imshow('Text', blank)

# img = cv.imread('Photos/cat1.jpg')
# cv.imshow('Cat', img)

cv.waitKey(0)