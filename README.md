```
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
```

## Input Files:
![img2](https://github.com/user-attachments/assets/557da028-5d2a-4226-83f6-425d47b2afba)


![img1](https://github.com/user-attachments/assets/a696146b-0b6c-4edc-ab5e-14b50a2a5f60)


## Output:
![final image 2](https://github.com/user-attachments/assets/e9471b7c-cfa8-480f-bee7-1b18671c4dd6)


![final image 1](https://github.com/user-attachments/assets/e3ef6d94-327e-4692-b8f8-b0a40a652b79)

![R1](https://github.com/user-attachments/assets/520f1092-283e-44d6-8542-5bb67632df18) ![R2](https://github.com/user-attachments/assets/64218f91-45d2-400b-a56d-f13152dfde18) ![R3](https://github.com/user-attachments/assets/b4417fcb-e7dd-4ffb-be0f-e5820bb78f21) ![R4](https://github.com/user-attachments/assets/18fb7b88-6d36-48ce-a11c-e16f55013b02)
![R5](https://github.com/user-attachments/assets/eb40b624-cb79-4e29-b87f-dd18a0d47497) ![R6](https://github.com/user-attachments/assets/35f8df2a-ba6d-4356-afc2-ea719504ac28) ![R7](https://github.com/user-attachments/assets/eb9a5b5f-3694-41ed-bcf8-087b13ced204) ![R8](https://github.com/user-attachments/assets/62313e3e-50df-446a-94a4-50ed9783fab8)







