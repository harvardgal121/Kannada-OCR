import copy
import cv2
import numpy as np
img = cv2.imread('Frontal.jpg', 0);
vis = copy.copy(img)
mser = cv2.MSER()
mser_areas=mser.detect(img)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('img', vis)
cv2.waitKey(0)
cv2.destroyAllWindows()