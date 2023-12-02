import cv2
import easyocr
import matplotlib.pyplot as plt


image_path = './R.jpg'

#read image
img = cv2.imread(image_path)
\

reader = easyocr.Reader(['en'], gpu=False)
try:
    text_ = reader.readtext(img)
    print(text_)
except Exception as e:
    print(f'Error: {e}')

for t in text_:
    bbox, text, score = t
    print(text)

    cv2.rectangle(img, bbox[0], bbox[2], (255, 0, 0), 2)
    cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()