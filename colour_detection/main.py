import cv2
import util
from PIL import Image

yellow = [0, 255, 255] # yellow in BGR colorspace
blue = [0, 255, 0] # blue in BGR colorspace
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera')
    exit()
    
while True:
    ret, frame = cap.read()
    
    # detect color
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    y_lower_limit, y_upper_limit = util.get_limits(color=yellow)
    b_lower_limit, b_upper_limit = util.get_limits(color=blue)
    y_mask = cv2.inRange(hsv_image, y_lower_limit, y_upper_limit)
    b_mask = cv2.inRange(hsv_image, b_lower_limit, b_upper_limit)

    # bouding box
    y_mask_ = Image.fromarray(y_mask)
    y_bounding_box = y_mask_.getbbox()
    b_mask_ = Image.fromarray(b_mask)
    b_bounding_box = b_mask_.getbbox()

    if y_bounding_box is not None:
        x1, y1, x2, y2 = y_bounding_box
        y_frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 4)
        # print('Yellow: ', y_bounding_box)

    if b_bounding_box is not None:
        x1, y1, x2, y2 = b_bounding_box
        b_frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        # print('Blue: ', b_bounding_box)

    window_name = 'frame'
    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()