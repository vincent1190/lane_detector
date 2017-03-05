# This is just al the imports that  are needed to be made
import numpy as np
import cv2
import os

#we set the variable of the path to were the video is. Change if using a different video
location=r"C:\\Python27\\Scripts\\road_vid.mp4"

#this object will take in frames from either video file or camera
#set to an index starting with 0 to select connected camera
#set arg to video file path to get from video
cap=cv2.VideoCapture(location)
#make sure you change this path when you use another vid

#You can also access some of the features of this video using cap.get(propId,value) method 
#where propId is a number from 0 to 18. Each number denotes a property of that video
ret=cap.set(3,320)
ret=cap.set(4,240)
cap.set(5,120)

#this simply gets that value of the video feature going by the propid
print cap.get(3)
print cap.get(4)

#this is justa check to see if the video is opened or not. If its opened,True else False
#when the program didn't seem to run, this told me that it wasn't even able to play the video
print cap.isOpened()

#this will only run the rest of the methods if the video is open else it'll 
#just end the program
while(cap.isOpened()):
# this will capture frame by frame 
    ret,frame=cap.read()
# this resizes the size of the video that will be shown. first arg is the source while the second is the width and height 
    small=cv2.resize(frame, (700, 400))
    #small=cv2.medianBlur(small,5)
     #"""may not have to resize other vids. if you dont resize make sure to change args on cvtColor,drawContours and imshow back to frame"""

# this changes the video to grayscale. the first arg is the image and the second arg is the color space it will be put in
#will have to change it to HSV to better capture the colors needed.(use gimp to capture the needed color range for the white line)
    gray=cv2.cvtColor(small,cv2.COLOR_BGR2GRAY)
	

    ret,thresh=cv2.threshold(gray,140,255,0)#original number was 125,255,0   /it is also 140,255,0
    #work on the threshold some more
	#this below is a different kind of threshold that will hopefully take out the noise in the lane detection
    #thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,20)
	
	#this retrieves contours from the image
	#first arg is the image, second arg is the retrievsl method. the last one is the approximation method
    contours, hierarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	#this will draw on the retrived contours and draws on them
	# first arg is the image to be drawn on, second arg is the retrieved contours 
	# 3rd arg is the contour index. -1 shows all contours,4th arg is color,5th is line width by pixel
    cv2.drawContours(small,contours,-1,(255,0,0),2)
    
	
# this block below simply names, positions and displays the different video outputs	
    cv2.imshow('highway',thresh)
    cv2.moveWindow('highway',400,300)
    cv2.imshow('contours',small)
    cv2.moveWindow('contours',50,0)
    cv2.imshow('gray',gray)
    cv2.moveWindow('gray',750,0)
# waitKey displays the image for specified milliseconds else it will display 
#the window infinitely till a key is pressed then it will move to the next frame
#when q is pressed, it will exit out of the program
    if cv2.waitKey(1) & 0xff==ord('q'):
       break
 
# Closes video file or capturing device 
cap.release()

#destroys all gui windows
cv2.destroyAllWindows()
    
