import pytesseract as pyt
import cv2

img=cv2.imread("image.jpg")

pyt.pytesseract.tesseract_cmd="D:\\tesseract\\tesseract.exe"

text =pyt.image_to_string(img)

print(text)