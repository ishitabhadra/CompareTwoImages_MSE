import cv2
import numpy as np
import matplotlib.pyplot as plt

# load the input images
img1 = cv2.imread('pho_6.png')
img2 = cv2.imread('voy_6.png')

img1_1 = cv2.imread('voy_6.png')
img2_1 = cv2.imread('pho_6.png')

# convert the images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img1_1 = cv2.cvtColor(img1_1, cv2.COLOR_BGR2GRAY)
img2_1 = cv2.cvtColor(img2_1, cv2.COLOR_BGR2GRAY)

# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)
#plt.imshow(diff)

error, diff = mse(img1_1, img2_1)
print("Image matching Error between the two images:",error)

plt.imshow(diff)
