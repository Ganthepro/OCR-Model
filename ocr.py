import easyocr
import cv2
from PIL import Image

img = cv2.imread(r"5.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
color = cv2.cvtColor(gray,cv2.COLOR_BGR2RGB)
im = Image.fromarray(color)
reader = easyocr.Reader(['th'],gpu=True)
read = reader.readtext(gray,detail=0)
plates = []

for i in read:
    chars = "ก ข ฃ ค ฅ ฆ ง จ ฉ ช ซ ฌ ญ ฎ ฏ ฐ ฑ ฒ ณ ด ต ถ ท ธ น บ ป ผ ฝ พ ฟ ภ ม ย ร ล ว ศ ษ ส ห ฬ อ ฮ"
    ints = "0 1 2 3 4 5 6 7 8 9"
    char = 0
    inte = 0
    for c in i:
        if c in chars.split(" "):
            char += 1
        elif c in ints.split(" "):
            inte += 1
    if char == 2 and inte >= 3:
        flag = False
        text = i
        for c in i:
            if c not in chars.split(" ") and c not in ints.split(" "):
                text = text.replace(c,"")
        plates.append(text)
        
print(plates)