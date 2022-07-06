import cv2
import numpy as np

image = cv2.imread(filename=r'obrazy/captcha.png')
img = image.copy()

# cv2.imshow(winname='image', mat=image)
# cv2.waitKey(delay=0)

height, width = img.shape[:2]
print(f"Wysokość: {height}")
print(f"Szerokość: {width}")

# linia
cv2.line(img=img, pt1=(0, 0), pt2=(width, height), color=(0, 255, 0), thickness=5)
cv2.imshow(winname='logo', mat=img)
cv2.waitKey(0)

# prostokąt
img = image.copy()
cv2.rectangle(img=img, pt1=(100, 50), pt2=(200, 100), color=(0, 255, 0), thickness=5)
cv2.imshow(winname='logo', mat=img)
cv2.waitKey(0)

#koło
img = image.copy()
cv2.circle(img=img, center=(200, 200), radius=90, color=(0, 255, 0), thickness=5)
cv2.imshow(winname='logo', mat=img)
cv2.waitKey(0)

#wielokąt bez domknięcia
img = image.copy()
pts = np.array([[50, 50], [100, 150], [280, 150], [200, 200], [50, 200]], dtype='int32').reshape((-1, 1, 2))
cv2.polylines(img=img, pts=[pts], isClosed=False, color=(0, 255, 0), thickness=5)
cv2.imshow('logo', mat=img)
cv2.waitKey(0)

#wielokąt z domknięciem
img = image.copy()
pts = np.array([[50, 50], [100, 150], [280, 150], [200, 200], [50, 200]], dtype='int32').reshape((-1, 1, 2))
cv2.polylines(img=img, pts=[pts], isClosed=True, color=(0, 255, 0), thickness=5)
cv2.imshow('logo', mat=img)
cv2.waitKey(0)

#dodanie tekstu
#wielokąt bez domknięcia
img = image.copy()
cv2.putText(img=img, text='captcha', org=(20, 40), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1.5, color=(255, 0, 0), thickness=2)

cv2.imshow('logo', mat=img)
cv2.waitKey(0)

