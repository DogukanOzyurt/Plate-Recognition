# -*- coding: utf-8 -*-
"""Plate_Recognition.ipynb


#1. Update data

#2.Choose an original image
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Defining image variables
N1 = plt.imread("N1.jpeg")
N2 = plt.imread("N2.jpeg")
N3 = plt.imread("N3.jpeg")
N4 = plt.imread("N4.jpeg")
N5 = plt.imread("N5.jpeg")
N6 = plt.imread("N6.jpeg")
N7 = plt.imread("N7.jpeg")
N8 = plt.imread("N8.jpeg")
N9 = plt.imread("N9.jpeg")
N10 = plt.imread("N10.jpeg")
N11 = plt.imread("N11.jpeg")
N12 = plt.imread("N12.jpeg")
N13 = plt.imread("N13.jpeg")
N14 = plt.imread("N14.jpeg")
N15 = plt.imread("N15.jpeg")
N16 = plt.imread("N16.jpeg")

# Create 4 row 4 column subplot
plt.subplots(4, 4, figsize=(20, 15))

# Plot images
for i in range(1, 17):
    plt.subplot(4, 4, i)
    plt.imshow(eval(f'N{i}'))
    plt.title('Image {}'.format(i))
    plt.axis('off')

plt.show()

"""Please choose which of the images above you want to use."""

print("Choose a number between 1-16")
x = int(input())
for i in range(1,17):
  if x == 1:
    image1 = plt.imread("N1.jpeg")
    image = cv2.imread("N1.jpeg")
  elif x == 2:
    image1 = plt.imread("N2.jpeg")
    image = cv2.imread("N2.jpeg")
  elif x == 3:
    image1 = plt.imread("N3.jpeg")
    image = cv2.imread("N3.jpeg")
  elif x == 4:
    image1 = plt.imread("N4.jpeg")
    image = cv2.imread("N4.jpeg")
  elif x == 5:
    image1 = plt.imread("N5.jpeg")
    image = cv2.imread("N5.jpeg")
  elif x == 6:
    image1 = plt.imread("N6.jpeg")
    image = cv2.imread("N6.jpeg")
  elif x == 7:
    image1 = plt.imread("N7.jpeg")
    image = cv2.imread("N7.jpeg")
  elif x == 8:
    image1 = plt.imread("N8.jpeg")
    image = cv2.imread("N8.jpeg")
  elif x == 9:
    image1 = plt.imread("N9.jpeg")
    image = cv2.imread("N9.jpeg")
  elif x == 10:
    image1 = plt.imread("N10.jpeg")
    image = cv2.imread("N10.jpeg")
  elif x == 11:
    image1 = plt.imread("N11.jpeg")
    image = cv2.imread("N11.jpeg")
  elif x == 12:
    image1 = plt.imread("N12.jpeg")
    image = cv2.imread("N12.jpeg")
  elif x == 13:
    image1 = plt.imread("N13.jpeg")
    image = cv2.imread("N13.jpeg")
  elif x == 14:
    image1 = plt.imread("N14.jpeg")
    image = cv2.imread("N14.jpeg")
  elif x == 15:
    image1 = plt.imread("N15.jpeg")
    image = cv2.imread("N15.jpeg")
  elif x == 16:
    image1 = plt.imread("N16.jpeg")
    image = cv2.imread("N16.jpeg")
  else:
    print("Please enter a number between 1-15.")
plt.imshow(image1)

"""#3.Apply the colour conversion from RGB image to grayscale image"""

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Print two images to the screen
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap="gray")
plt.title('Grayscale Image')
plt.axis('off')


plt.show()

"""#4.Apply the image segmentation using Otsu’s thresholding"""

# Histogram Gray
h = np.zeros((256,))
[rows,cols] = gray_image.shape

for i in range(rows):
    for j in range(cols):
        pix = gray_image[i,j]
        h[pix] = h[pix] + 1

plt.bar(range(256),h)
plt.title("Gray Histogram")
plt.xlabel('Pixel Values')
plt.ylabel('Frequency')
plt.show()

# Add up the pixel numbers corresponding to each pixel value in the histogram.

total_pixels = np.sum(h)
h

# Calculating Weighted Probabilities and Cumulative Probabilities

probabilities = h / total_pixels
cumulative_probabilities = np.cumsum(probabilities)
print(probabilities)
print(cumulative_probabilities)

# Calculating Class Means and Total Variance

class_means = np.cumsum(probabilities * np.arange(0, 256))
global_mean = class_means[-1]

between_class_variance = (total_pixels * np.power(global_mean * cumulative_probabilities - class_means, 2))
print(class_means)
print(global_mean)
print(between_class_variance)

# Choosing the Best Threshold Value
optimal_threshold = np.argmax(between_class_variance) + 20
print(optimal_threshold)

# Thresholding Application
_, binary_image = cv2.threshold(gray_image, optimal_threshold, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Otsu Thresholding')
plt.axis('off')

plt.show()

"""#5.Apply the noise removal and image subtraction"""

# Erosion
#kernel = np.ones((3,3),np.uint8)
#erosion = cv2.erode(binary_image, kernel)
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # square_kernel

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)) # rect_kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) # rect_kernel



# Dilation
dilation = cv2.dilate(binary_image, kernel1, iterations=2)
erosion = cv2.erode(binary_image, kernel, iterations=1)


plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(binary_image, cmap='gray')
plt.title("Otsu Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(dilation, cmap="gray")
plt.title("Otsu Image with Dilation")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(erosion, cmap="gray")
plt.title("Otsu Image with Erosion")
plt.axis("off")


plt.show()

"""#6.Draw the bounding box

"""

# Find contours
contours, _ = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Colorize the image
color_image = cv2.cvtColor(erosion, cv2.COLOR_GRAY2BGR)

# Draw the contours
cv2.drawContours(color_image, contours, -1, (0, 255, 0), 10)

# Show images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(erosion, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(color_image)
plt.title('Contours')

plt.show()

import cv2
import matplotlib.pyplot as plt

# Find contours
contours, _ = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Colorize the image
color_image = cv2.cvtColor(erosion, cv2.COLOR_GRAY2BGR)

# Draw the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(color_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show images
plt.figure(figsize=(10, 5))


plt.imshow(color_image)
plt.title('Contours with Bounding Boxes')

plt.show()

import cv2
import matplotlib.pyplot as plt

# Find contours
contours, _ = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Colorize the image
color_image = cv2.cvtColor(erosion, cv2.COLOR_GRAY2BGR)

# Bottom edges
h1, w1 = erosion.shape

# Draw the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    # Check width and height conditions
    if 3 <= w/h <= 5 and x > 10 and y > 10 and (x+w) < (w1-10) and (y+h) < (h1-10):
        # Draw a rectangle
        cv2.rectangle(color_image, (x, y), (x+w, y+h), (0, 255, 0), 2)


# Show images
plt.figure(figsize=(10, 5))


plt.imshow(color_image)
plt.title('Contours with Bounding Boxes')

plt.show()

"""#7.Perform the image cropping"""

import cv2
import matplotlib.pyplot as plt



# Find contours
contours, _ = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0
max_contour = None

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    # Check width and height conditions
    if 3 <= w/h <= 5 and x > 10 and y > 10 and (x+w) < (w1-10) and (y+h) < (h1-10):
        # Calculate area
        area = w * h

        # Update largest area and stroke
        if area > max_area:
            max_area = area
            max_contour = contour

# Draw the largest rectangle
if max_contour is not None:
    x, y, w, h = cv2.boundingRect(max_contour)

    if x > 10 and y > 10 and (x+w) < (w1-10) and (y+h) < (h1-10):

      # Draw largest rectangle on color image
      cv2.rectangle(erosion, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Crop image according to coordinates
cropped_image = erosion[y:y+h, x:x+w]

# Show cropped image
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')
plt.show()

import cv2
import matplotlib.pyplot as plt


# Dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated_image1 = cv2.dilate(cropped_image, kernel, iterations=2)

# Show images

plt.imshow(dilated_image1, cmap='gray')
plt.title('Dilated Image')

plt.show()

import cv2
import matplotlib.pyplot as plt

# Erosion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
eroded_image1 = cv2.erode(dilated_image1, kernel, iterations=1)

# Show image

plt.imshow(eroded_image1, cmap='gray')
plt.title('Eroded Image')
plt.show()

"""#8.Apply the optical character recognition method

We define the keras_ocr library for optical character recognition
"""

!pip install keras_ocr

import keras_ocr

# Create Keras OCR Pipeline
pipeline = keras_ocr.pipeline.Pipeline()

# Convert image to RGB color space
# Almost all CNN algorithms and keras_ocr work on rbg
cropped_image_rgb = cv2.cvtColor(eroded_image1, cv2.COLOR_BGR2RGB)

# Use grayscale image
prediction_groups = pipeline.recognize([cropped_image_rgb])

# Show results
image_with_predictions = keras_ocr.tools.drawAnnotations(image=cropped_image_rgb, predictions=prediction_groups[0])

# print results
result_text = ' '.join([word_info[0] for word_info in prediction_groups[0]])
print(result_text)

