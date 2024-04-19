import numpy, time, cv2

video=cv2.VideoCapture('images/video.mp4')
print(video.read())

count=0
background=0

for i in range(60):
    return_value, background=video.read()

while(video.isOpened()):
    return_value, img=video.read()
    if return_value==False:
        break
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    upper_red=numpy.array([100,255,255])
    lower_red=numpy.array([100,40,40])
    mask1=cv2.inRange(hsv,lower_red,upper_red)

    upper_red=numpy.array([180,255,255])
    lower_red=numpy.array([150,40,40])
    mask2=cv2.inRange(hsv,lower_red,upper_red)

    mask1=mask1+mask2

    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=2,)
    mask1=cv2.dilate(mask1,numpy.ones((3,3),numpy.uint8),iterations=1)
    mask2=cv2.bitwise_not(mask1)
    res1=cv2.bitwise_and(background,background,mask=mask1)
    res2=cv2.bitwise_and(img,img,mask=mask2)
    final=cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('final video',final)
    k=cv2.waitKey(10)
    if k==27:
        break
