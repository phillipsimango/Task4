# Phillip Simango - C17341516

# 1. Open any image;
# 2. Crop out the fourth quadrant of the image;
# 3. Rotate the cropped section by 45 degrees;

import cv2

# 1. Open any image;
I = cv2.imread('/Users/phillipsimango/OneDrive/Image Processing/TransformationTasks/photo.jpg')

# 2. Crop out the fourth quadrant of the image i.e. bottom right-hand corner of the image; original image size: 325x485
C = I[243:485, 113:325]

# 3. Rotate the cropped section by 45 degrees;
(cols, rows) = C.shape[:2]  # getting the matrix dimensions of cropped image C
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)  # Parameters (image center, angle of rotation, scaling factor)
R = cv2.warpAffine(C, M, (cols, rows))

cv2.imshow("Original Image", I)
cv2.waitKey()  # Waits for key to be pressed before showing next image
cv2.imshow("Cropped Image", C)
cv2.waitKey()   # Waits for key to be pressed before showing next image
cv2.imshow("Cropped Rotated Image", R)
cv2.waitKey()   # Waits for key to be pressed before showing next image
