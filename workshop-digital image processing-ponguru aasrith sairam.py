import cv2

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

row, col = img1.shape[:2]
row2, col2 = row//2, col//2

quad1_img1 = img1[:row2, :col2]
quad2_img1 = img1[:row2, col2:]
quad3_img1 = img1[row2:, :col2]
quad4_img1 = img1[row2:, col2:]

quad1_img2 = img2[:row2, :col2]
quad2_img2 = img2[:row2, col2:]
quad3_img2 = img2[row2:, :col2]
quad4_img2 = img2[row2:, col2:]

cv2.imwrite('R1.jpg', quad1_img1)
cv2.imwrite('R2.jpg', quad2_img1)
cv2.imwrite('R3.jpg', quad3_img1)
cv2.imwrite('R4.jpg', quad4_img1)

cv2.imwrite('R5.jpg', quad1_img2)
cv2.imwrite('R6.jpg', quad2_img2)
cv2.imwrite('R7.jpg', quad3_img2)
cv2.imwrite('R8.jpg', quad4_img2)

quad1_img1, quad1_img2 = quad1_img2, quad1_img1
quad2_img1, quad2_img2 = quad2_img2, quad2_img1
quad3_img1, quad3_img2 = quad3_img2, quad3_img1
quad4_img1, quad4_img2 = quad4_img2, quad4_img1

reg_num = 212223240116
width, height = int(str(reg_num)[-4:]), int(str(reg_num)[-4:])


if width % 2 != 0 or height % 2 != 0:
    width += 1
    height += 1


final_img1 = cv2.resize(quad1_img1, (width, height))
final_img2 = cv2.resize(quad1_img2, (width, height))

cv2.imwrite('final_img1.jpg', final_img1)
cv2.imwrite('final_img2.jpg', final_img2)