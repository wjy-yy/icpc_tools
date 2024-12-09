import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 设置写入文字名和读取文件名
add_text = "opencv+Pillow"
file_bk_img = "Contestant.png"

bk_img = cv2.imread(file_bk_img)  
# 设置需要显示的字体
fontpath = "Arial Bold.ttf"
font = ImageFont.truetype(fontpath, 180)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
# 绘制文字信息
draw.text((1063, 1535),  add_text, font=font,
          fill=(255, 255, 255), anchor="mm",
          align="center")
bk_img = np.array(img_pil)

# cv2.imshow("add_text", bk_img)
# cv2.waitKey()
cv2.imwrite(add_text+".png", bk_img)