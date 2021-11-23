import cv2
import random
import math
import numpy as np


def random_erasing(img,mean = [0.4914, 0.4822, 0.4465],sl = 0.02,sh = 0.4,r1 = 0.3):

    """sl: min erasing area
    sh: max erasing area
    r1: min aspect ratio
    mean: erasing value"""

    img = img.copy()
    

    for attempt in range(100):
        area = img.shape[0] * img.shape[1]
    
        target_area = random.uniform(sl, sh) * area
        aspect_ratio = random.uniform(r1, 1/r1)

        h = int(round(math.sqrt(target_area * aspect_ratio)))
        w = int(round(math.sqrt(target_area / aspect_ratio)))

        if w < img.shape[1] and h < img.shape[0]:
            x1 = random.randint(0, img.shape[0] - h)
            y1 = random.randint(0, img.shape[1] - w)
            if img.shape[2] == 3:
                img[ x1:x1+h, y1:y1+w , 0] = mean[0]
                img[x1:x1+h, y1:y1+w, 1] = mean[1]
                img[ x1:x1+h, y1:y1+w, 2] = mean[2]
            else:
                img[ x1:x1+h, y1:y1+w,0] = mean[0]
            return img

    return img


image = cv2.imread("img/a.jpg")

for i in range(5):
    imgAug = random_erasing(image)
    cv2.imshow(f"{i}",imgAug)

cv2.waitKey(0)
cv2.destroyAllWindows()