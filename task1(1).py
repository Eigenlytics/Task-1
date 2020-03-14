#!/usr/bin/env python
# coding: utf-8

# In[30]:


import cv2
import numpy as np
import os
import sys
from PIL import Image

img = cv2.imread('img22.jpg')
print(img)

graysc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#retval, threshold2 = cv2.threshold(graysc, 160, 255, cv2.THRESH_BINARY)

block_size = 11
constant = 2
th1 = cv2.adaptiveThreshold(graysc, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)

contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print ("Number of Contours = "+ str(len(contours)))

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

for contour in contours:

    [x, y, w, h] = cv2.boundingRect(contour)


    if h > 300 and w > 300:
        continue


    if h < 20 or w < 12:
        continue


    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
# write original image with added contours to disk

cv2.imwrite("contoured.jpg", img)

cv2.imshow('Current Image', img)
cv2.imshow('gray scale', graysc)
#cv2.imshow('adaptive thresh', th1)
#cv2.imshow('threshold2', threshold2)
cv2.waitKey(0)

cv2.destroyAllWindows()

contours_vec = np.reshape(contours, -1)
print(contours_vec)
print(contours_vec.shape)

path = "D:\STUDY\INTERNSHIP\Task 1\Logo Database"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((256,256), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()


# In[ ]:




