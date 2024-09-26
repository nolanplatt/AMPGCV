from ultralytics import YOLO
import cv2
import numpy as np
model = YOLO('*INSERT MODEL NAME*')
listOfImages = []
for im in listOfImages:
    results = model(im, save = False)
    height, width, _ = cv2.imread(im).shape
    xplusy, xminusy = dict(), dict()
    masks = results[0].masks.segments # Masks object for segmenation masks outputs for seg in masks [0]:
    for seg in masks[0]:
        val1, val2 = seg [0] + seg [1], seg [0] - seg [1]
        xplusy[tuple([seg [0], seg[1]])] = val1
        xminusy [tuple([seg [0], seg [1]])] = val2
    temp1, temp2, temp3, temp4 = min(xplusy.values()), max(xplusy.values()), min (xminusy.values()), max(xminusy.values()) 
    res1 = [key for key in xplusy if xplusy [key] == temp1] 
    res2 = [key for key in xplusy if xplusy [key] ==temp2]
    res3 = [key for key in xminusy if xminusy [key] ==temp3]
    res4 = [key for key in xminusy if xminusy [key] == temp4]
    img = cv2.imread(im)
    minxy= (int(res1[0][0]*width), int(res1[0] [1] *height)) 
    maxxy = (int(res2 [0][0] *width), int(res2 [0] [1] *height)) 
    minxmy = (int(res3 [0] [0] * width), int(res3 [0] [1] *height)) 
    maxxmy = (int(res4 [0][0] *width), int (res4 [0] [1] *height))
    plantTopLeft = [int(res1[0][0]*width), int (res1[0] [1] *height)]
    plantBottomRight = [int(res2 [0][0] *width), int (res2 [0] [1] *height)]
    plantBottomLeft = [int(res3 [0][0]*width), int (res3 [0] [1] *height)]
    plantTopRight = [int(res4 [0][0] *width), int(res4 [0] [1] *height)]
    x_min = min(plantTopLeft[0], plantBottomLeft[0])
    x_max = max(plantTopRight[0], plantBottomRight[0])
    y_min = min(plantTopLeft[1], plantTopRight[1])
    y_max = max(plantBottomLeft[1], plantBottomRight[1])
    cropped_image = img[y_min:y_max, x_min:x_max]
    cv2.imwrite(f'FILE NAME HERE', cropped_image)
