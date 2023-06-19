import pytesseract
import PIL.Image
import cv2

'''
page segmentation modes:
0 orientation and script detection (osd) only.
1 automati page segmentation with osd.
2 automatic page segmentation, but no osd, or ocr.
3 fully automatic page segmentation, but no osd. (default)
4 assume a single column of text of variable sizes.
5 assume a single uniform block of vertically aligned text.
6 assume a single uniform block of text.
7 treat the image as a single text line.
8 treat the image as a single word.
9 treat the image as a single word in a circle.
10 treat the image as a single character.
11 sparse text. find as much text as possible in no particular order.
12 sparse text with osd.
13 raw line. treat the image as a single text line, bypassing hacks that are tesseract specific.
'''

'''
ocr engine mode:
0 legacy engine only.
1 neural net lstm engine only.
2 legacy + lstm engines.
3 default, based on what is available.
'''

myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("image3.jpg"), config=myconfig)

#print(text)

file = open('note1.txt','w')

file.write(text)
file.close()




