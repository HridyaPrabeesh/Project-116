import cv2

cv2.imread("C:\Users\Hridya\Desktop\pROJECT 116\solar-system.jpg")

cv2.putText(img,"Sun",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Venus",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Mercury",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Mars",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Earth",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Jupiter",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Saturn",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Neptune",(200,300),cv2.FONT_HERSHLEY_COMPLEX,0.5,(255,255,255))


cv2.imshow("Output",img) 

cv2.waitKey(0)
