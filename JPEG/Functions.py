import cv2
import numpy as np
import os

os.system("cls")

image = np.round(np.random.rand(16, 16) * 100, decimals=2)
block_size = 8


def Image_2_blocks(image, block_size):
    blocks = np.zeros(
        (
            block_size,
            block_size,
            int(image.shape[0] / block_size),
            int(image.shape[1] / block_size),
        ),
    )
    x = y = 0
    for i in range(0, image.shape[0], block_size):
        y = 0
        for j in range(0, image.shape[1], block_size):
            blocks[:, :, x, y] = image[i : i + block_size, j : j + block_size]
            y += 1
        x += 1
    return blocks


def Blocks_2_Image(blocks, block_size):
    image_recons = np.zeros(
        (blocks.shape[0] * blocks.shape[2], blocks.shape[1] * blocks.shape[3])
    )
    x = y = 0
    for i in range(0, image_recons.shape[0], block_size):
        y = 0
        for j in range(0, image_recons.shape[1], block_size):
            image_recons[i : i + block_size, j : j + block_size] = blocks[:, :, x, y]
            y += 1
        x += 1
    return image_recons
