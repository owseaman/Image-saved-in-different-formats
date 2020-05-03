''' Read an input image and save the image in the following colour spaces.
- HSV colour space - cv2.COLOR_RGB2HSV
- YCrCb colour space - COLOR_BGR2YCrCb
- Lab colour space - COLOR_BGR2Lab
2. Record a 10 second video of yourself waving your hand, in grayscale.'''

import cv2
#import sys
#imagePath = r'C:\Users\Owoeye\Pictures\2020_04_25\JD.JPG'
imagePath = 'C:\\Users\\Owoeye\\Desktop\\Soft\\JoSax OCR\\JD.JPG'
img = cv2.imread(imagePath)
if img is None:
    sys.exit('Could not read the image')
cv2.namedWindow('JD', cv2.WINDOW_NORMAL)
cv2.imshow('JD', img)
k = cv2.waitKey(0)
if k == ord('s'):
    #isp = 'C:/Users/Owoeye/Desktop/Soft/JoSax OCR'
    #cv2.imwrite(isp + 'savedJD.png', img)
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ycrcbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    labImage = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

    cv2.imwrite('C:/Users/Owoeye/Desktop/Soft/JoSax OCR/savedJD.png', img)
    cv2.imwrite('C:/Users/Owoeye/Desktop/Soft/JoSax OCR/gray_savedJD.png', grayImage)
    cv2.imwrite('C:/Users/Owoeye/Desktop/Soft/JoSax OCR/hsv_savedJD.png', hsvImage)
    cv2.imwrite('C:/Users/Owoeye/Desktop/Soft/JoSax OCR/ycrcb_savedJD.png', ycrcbImage)
    cv2.imwrite('C:/Users/Owoeye/Desktop/Soft/JoSax OCR/lab_savedJD.png', labImage)


