# -*- coding: utf-8 -*-
"""Data Augmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1diki-UhChHiVhX3IbmDzucRr_oTkT3YE
"""

import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    datagen = ImageDataGenerator(
        rotation_range=30,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        fill_mode='nearest'
    )

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path)
            if image is None:
                print(f"Failed to read {img_path}. Skipping...")
                continue
            image = image.reshape((1,) + image.shape)

            for i, augmented_image in enumerate(datagen.flow(image, batch_size=1)):
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_aug_{i}.jpg")
                cv2.imwrite(output_path, augmented_image[0])

                if i >= 5:
                    break


input_folder_path = '/content/drive/MyDrive/dummy_folders/JPEGImages'
output_folder_path = '/content/drive/MyDrive/BCCD/Augmented_images'
process_images(input_folder_path, output_folder_path)

