import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas

df = pandas.read_excel("Volunteer.xlsx")
conf = 'Volunteer'
# conf = 'Coach'

for idx, data in df.iterrows():
    # if idx != 3:
    #     continue
    # print(data.__getitem__(1))
    # print(data['Team Name'])
    # 设置写入文字名和读取文件名
    file_bk_img = conf+".png"
    if conf == 'Contestant' or data['No'] == 1:
        offset = 0
    else:
        offset = -200
    bk_img = cv2.imread(file_bk_img)  
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # =======队伍名
    if conf == 'Contestant' or data['No'] == 1:
        add_text = data['Team Name']
    # 设置需要显示的字体
        fontpath = "Arial Bold Italic.ttf"
        if len(add_text) > 20:
            font = ImageFont.truetype(fontpath, max(50,90-len(add_text)//2))
        else:
            font = ImageFont.truetype(fontpath, 80)
        draw.text((1063, 1800),  add_text, font=font,
            fill=(255, 255, 255), anchor="mm",
            align="center")
    # 绘制文字信息
    fontpath = "Arial Bold.ttf"
    # =======学校名
    add_text = data['Institution Name']
    if '\n' in add_text:
        text1, text2 = add_text.split('\n')
        if max(len(text1),len(text2)) > 20:
            font = ImageFont.truetype(fontpath, 130-max(len(text1),len(text2)))
        else:
            font = ImageFont.truetype(fontpath, 110)
        draw.text((1063, 2000+offset),  text1, font=font,
                fill=(255, 255, 255), anchor="mm",
                align="center")
        draw.text((1063, 2150+offset),  text2, font=font,
                fill=(255, 255, 255), anchor="mm",
                align="center")
    else:
        if len(add_text) > 20:
            font = ImageFont.truetype(fontpath, 130-len(add_text))
        else:
            font = ImageFont.truetype(fontpath, 110)
        draw.text((1063, 2000+offset),  add_text, font=font,
                fill=(255, 255, 255), anchor="mm",
                align="center")
    bk_img = np.array(img_pil)
    if conf == 'Contestant' or conf == 'Volunteer' or conf == 'Technical':
        for i in range(1,4):
            if type(data['Member '+str(i)+' Name']) == str or i==1:
                add_text = data['Member '+str(i)+' Name'] if type(data['Member '+str(i)+' Name']) == str else ''
                if len(add_text) > 15:
                    font = ImageFont.truetype(fontpath, 215-3*len(add_text))
                else:
                    font = ImageFont.truetype(fontpath, 200)
                img_pil = Image.fromarray(bk_img)
                draw = ImageDraw.Draw(img_pil)
                # 绘制文字信息
                draw.text((1063, 1535),  add_text, font=font,
                        fill=(255, 255, 255), anchor="mm",
                        align="center")
                font = ImageFont.truetype(fontpath, 110)
                draw.text((1063, 1300),  conf, font=font,
                        fill=(255, 255, 255), anchor="mm",
                        align="center")
                _img = np.array(img_pil)
                cv2.imwrite(conf+'/'+str(idx)+str(i)+".png", _img)
    else:
        add_text = data[conf+' Name']
        if len(add_text) > 15:
            font = ImageFont.truetype(fontpath, 215-3*len(add_text))
        else:
            font = ImageFont.truetype(fontpath, 200)
        img_pil = Image.fromarray(bk_img)
        draw = ImageDraw.Draw(img_pil)
        # 绘制文字信息
        draw.text((1063, 1535),  add_text, font=font,
                fill=(255, 255, 255), anchor="mm",
                align="center")
        font = ImageFont.truetype(fontpath, 110)
        draw.text((1063, 1300),  conf, font=font,
                fill=(255, 255, 255), anchor="mm",
                align="center")
        _img = np.array(img_pil)
        cv2.imwrite(conf+'/-'+str(idx)+".png", _img)
    # exit(0)

