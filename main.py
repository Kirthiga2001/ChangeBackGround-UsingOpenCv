import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_FPS,70)
segmenter=SelfiSegmentation(1)
fps=cvzone.FPS()

index=1
while 1:
    path="Images/"+str(index)+".jpg"
    imgbg = cv2.imread(path)
    if index>8:
        index=1
    elif index<1:
        index=8
    s,img=cap.read()
    imgout=segmenter.removeBG(img,imgbg,threshold=0.25)

    joinimg=cvzone.stackImages([img,imgout],2,1)
    Fps,joinimg=fps.update(joinimg,scale=1)
    cv2.imshow("Image", joinimg)
    k = cv2.waitKey(1)
    if k==ord('d'):
        index+=1
    elif k==ord('a'):
        index-=1
    elif k==ord('w'):
        break
