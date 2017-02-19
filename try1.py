
import numpy as np
import cv2
import copy
img=cv2.imread('signboard2.jpg', 0)

screen_res = 1280, 720
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt', window_width, window_height)

vis = copy.copy(img)


mser=cv2.MSER()
regions=mser.detect(img)
#print regions[1]
#print type(regions)
#print len(regions[1])
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
# for k in hulls:
# 	x, y, width, height = cv2.boundingRect(k)
# 	roi = img[y:y+height, x:x+width]
# 	cv2.imwrite(str(k)+".png", roi)
print hulls[10][0][0]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('dst_rt', vis)
cv2.waitKey(0)
cv2.destroyWindow('dst_rt')
