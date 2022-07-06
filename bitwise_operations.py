import cv2
import imutils

img1 = cv2.imread(r'obrazy/captcha.png')
img2 = cv2.imread(r'obrazy/captcha2.png')
img2 = imutils.resize(img2, height=220, width=200)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)

#wycięcie obszaru roi - region of interest
rows, cols, channels = img2.shape
roi = img1[:rows, :cols]
# cv2.imshow('roi', roi)


gray = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('grey', gray)


mask = cv2.threshold(src=gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv', mask_inv)


img_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)
img_fg = cv2.bitwise_and(src1=img2, src2=img2, mask=mask_inv)
cv2.imshow('img_bg', img_bg)
cv2.imshow('img_fg', img_fg)


dst = cv2.add(src1=img_bg, src2=img_fg)
img1[:rows, :cols] = dst
cv2.imshow('out', dst)
cv2.waitKey(0)

