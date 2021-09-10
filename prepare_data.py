import os
import numpy as np
from typing import List
import shutil
import torch
from PIL import Image
from torchvision import transforms
import glob

# Split ./BCCD_410 into train and test set


BCCD_Path = "./BCCD_410/"
Out_Path = "./BCCD_410_split/"
final_path = Out_Path

splits = [(0.6,'Train'),(0.4,'Test')]

def cp_files(files : List[str],src_dir : str, des_dir : str) -> None:
    for file in files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(des_dir,file),)


if not os.path.exists(Out_Path):
    os.makedirs(Out_Path, exist_ok=True)
for split in splits:
    os.makedirs(os.path.join(Out_Path, split[1]),exist_ok = True)

##### First Create the data splits #######
# labels = os.listdir(BCCD_Path)
labels = glob.glob(os.path.join(BCCD_Path, "*"))
labels = [label.split('/')[-1] for label in labels]
labels.sort()
print(labels)

np.random.seed(42)
torch.manual_seed(42)

for label in labels:
    images = os.listdir(os.path.join(BCCD_Path, label))
    images.sort()
    np.random.shuffle(images)
    
    prev_index = 0

    for split in splits:
    
        final_label_path = os.path.join(final_path, split[1], label)
        if not os.path.exists(final_label_path):
            os.makedirs(final_label_path,exist_ok = True)

        end_index = int(split[0] * len(images)) + prev_index
        print(end_index - prev_index)
        cp_files(images[prev_index:end_index], src_dir = os.path.join(BCCD_Path, label), des_dir = final_label_path)
        prev_index = end_index

print('Data Transfer Complete')