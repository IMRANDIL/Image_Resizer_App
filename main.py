import cv2

src = cv2.imread('user.jpg', cv2.IMREAD_UNCHANGED)
dest = 'newUser.png'
scale_percent = 50

# calcualte the 50 percent of original diamension
width = int(src.shape[1] * scale_percent/100)
height = int(src.shape[0] * scale_percent/100)

#dsize
dsize = (width, height)

#resize image
output = cv2.resize(src, dsize)

#output the new img

cv2.imwrite(dest, output)

