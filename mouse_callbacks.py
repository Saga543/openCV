import cv2

img = cv2.imread(r'Obrazy/captcha.png')
cv2.imshow('img', img)
cv2.waitKey(0)

