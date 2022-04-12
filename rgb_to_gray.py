# Muhamad Putra Satria
# F55120009
import cv2
img = cv2.imread("spongebob.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Api Original", img)
cv2.imshow("Gambar Api Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()