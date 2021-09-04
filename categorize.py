"""
Separate the 410 image into 5 categories: 
    ['EOSINOPHIL','LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL', 'BASOPHIL']

The categorization is provided by labels.csv
Images that contain 2 or more WBC's are excluded

Final Directory Structue (348 Images Total):
./BCCD_410
+---BASOPHIL
    +--- 3  '*.jpg' images
+---EOSINOPHIL
    +--- 87 '*.jpg' images
+---LYMPHOCYTE
    +--- 33 '*.jpg' images
+---MONOCYTE
    +--- 20 '*.jpg' images
+---NEUTROPHIL
    +--- 205 '*.jpg' images

4 images are missing:
['BloodImage_00116.jpg', 'BloodImage_00176.jpg', 'BloodImage_00280.jpg', 'BloodImage_00329.jpg']
"""

import os, sys, random
import csv
from glob import glob
import pandas as pd
from PIL import Image


IMG_DIR = "./BCCD/JPEGImages/"
DEST_DIR = "./BCCD_410/"
LABEL_CSV = "./labels.csv"
CATEGORIES = ['EOSINOPHIL','LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL', 'BASOPHIL']

# Make destination directories
os.mkdir(DEST_DIR)
for cat in CATEGORIES:
    os.mkdir(os.path.join(DEST_DIR, cat))

PREFIX = "BloodImage_00"
with open('labels.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    void_files = []     # Store non-existant image files
    for row in reader:
        id = row[0].split(',')[1].zfill(3)      # Image | 0 -- 410
        cat = row[0].split(',')[2]              # EOSINOPHIL | LYMPHOCYTE | ...
        if id == 'Image' or not cat or len(cat) > 10: continue

        path = os.path.join(IMG_DIR, PREFIX+id+'.jpg')
        try:
            image = Image.open(path)
            # print(os.path.join(DEST_DIR, cat, id))
            # image = Image.open(path).resize((128,128))  # Optionally resize images
            image.save(os.path.join(DEST_DIR, cat, id+'.jpg'))
        except FileNotFoundError:
            void_files.append(path.split('/')[-1])

print('Final directory contains: {} images:'.format(len(glob('./BCCD_410/*/*.jpg'))))
for cat in CATEGORIES:
    print('{}:{}'.format(cat, len(glob('./BCCD_410/'+cat+'/*.jpg'))))
print('{} images are missing:'.format(len(void_files)))
print(void_files)









            

