import numpy as np
import cv2
import matplotlib.pyplot as plt #plt.plot(x,y) plt.show()
import copy

gray = cv2.imread('Frontal.jpg', 0)
mser = cv2.MSER()


vis = copy.copy(gray)

regions = mser.detect(gray, None)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0)) 
# cv2.putText(vis, str('change'), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
# cv2.fillPoly(vis, hulls, (0, 255, 0))


# cv2.imwrite("t", vis)    
cv2.imshow('img', vis)
cv2.waitKey(0)
cv2.destroyAllWindows()