import os
import shutil
import cv2
import numpy as np

all_dir = r'./images'
ok_dir = r'./w'
ng_dir = r'./s'
# all_dir = r'D:\宁德时代\data\all_data\data\test\ok_10_30\pictures\images'
# ok_dir = r'D:\宁德时代\data\all_data\data\test\ok_10_30\pictures\w'
# ng_dir = r'D:\宁德时代\data\all_data\data\test\ok_10_30\pictures\s'

window_name = 'classify'
cv2.namedWindow(window_name,0)

index = 0
all_images = [os.path.join(all_dir,image) for image in os.listdir(all_dir)]
while True:
    if index < 0:
        index = 0
    elif index > len(all_images) - 1:
        index = len(all_images) - 1
    full_path = all_images[index]
    image = cv2.imdecode(np.fromfile(full_path,dtype=np.uint8),-1)
    cv2.imshow(window_name,image)
    key = cv2.waitKey(0)
    if key == ord('w'):
        image_name = os.path.split(full_path)[1]
        tmp_path = os.path.join(ok_dir,image_name)
        shutil.move(all_images[index],tmp_path)
        all_images[index] = tmp_path
        index += 1
    if key == ord('s'):
        image_name = os.path.split(full_path)[1]
        tmp_path = os.path.join(ng_dir,image_name)
        shutil.move(all_images[index],tmp_path)
        all_images[index] = tmp_path
        index += 1
    if key == ord('a'):
        index -= 1
    if key == ord('d'):
        index += 1
    if key == 27:
        break

    


