import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas

df = pandas.read_excel("中英文对照.xlsx")
# conf = 'Volunteer'
# conf = 'Coach'

for idx, data in df.iterrows():
    file_bk_img = data['Color']+"_back.png"
    bk_img = cv2.imread(file_bk_img)  
    img_pil = Image.fromarray(bk_img)
    fg_img = cv2.imread('name/'+data['Chinese']+'.jpg')  
    fg_pil = Image.fromarray(fg_img).resize((200, 200))

    img_pil.paste(fg_pil, (192, 200))
    if data['Rand'] == '*':
        fg_img = cv2.imread('star.png',cv2.IMREAD_UNCHANGED)  
        fg_pil = Image.fromarray(fg_img).convert('RGBA')#.resize((200, 200))
        r, g, b, a = fg_pil.split()
        img_pil.paste(fg_pil, (1691, 970),mask=a)
    offset = 0
    draw = ImageDraw.Draw(img_pil)

    add_text = 'Designed by wjyyy'
    # 设置需要显示的字体
    fontpath = "Arial Bold.ttf"
    font = ImageFont.truetype(fontpath, 40)
    draw.text((3200, 20),  add_text, font=font,
        fill=(237, 237, 237), anchor="mm",
        align="center")

    add_text = '/home/'+data['Seat']+'/'
    # 设置需要显示的字体
    fontpath = "Courier New Bold.ttf"
    font = ImageFont.truetype(fontpath, 110)
    draw.text((2200, 600),  add_text, font=font,
        fill=(119, 128, 133), anchor="mm",
        align="center")
    # =======队伍名
    add_text = data['Team Name']
    # 设置需要显示的字体
    fontpath = "Arial Bold Italic.ttf"
    if len(add_text) > 20:
        font = ImageFont.truetype(fontpath, max(67,126-len(add_text)//2))
    else:
        font = ImageFont.truetype(fontpath, 120)
    draw.text((1771, 1200),  add_text, font=font,
        fill=(110, 138, 143), anchor="mm",
        align="center")
    # 绘制文字信息
    fontpath = "Arial Bold.ttf"
    # =======学校名
    add_text = data['Institution Name']
    if '\n' in add_text:
        text1, text2 = add_text.split('\n')
        if max(len(text1),len(text2)) > 20:
            font = ImageFont.truetype(fontpath, 175-max(len(text1),len(text2)))
        else:
            font = ImageFont.truetype(fontpath, 145)
        draw.text((1771, 1400),  text1, font=font,
                fill=(12, 15, 17), anchor="mm",
                align="center")
        draw.text((1771, 1550),  text2, font=font,
                fill=(12, 15, 17), anchor="mm",
                align="center")
    else:
        if len(add_text) > 20:
            font = ImageFont.truetype(fontpath, 160-len(add_text))
        else:
            font = ImageFont.truetype(fontpath, 130)
        draw.text((1771, 1400+offset),  add_text, font=font,
                fill=(12, 15, 17), anchor="mm",
                align="center")
    bk_img = np.array(img_pil)
    cv2.imwrite('Team/'+str(idx)+".png", bk_img)
    # if conf == 'Contestant' or conf == 'Volunteer' or conf == 'Technical':
    #     for i in range(1,4):
    #         if type(data['Member '+str(i)+' Name']) == str or i==1:
    #             add_text = data['Member '+str(i)+' Name'] if type(data['Member '+str(i)+' Name']) == str else ''
    #             if len(add_text) > 15:
    #                 font = ImageFont.truetype(fontpath, 215-3*len(add_text))
    #             else:
    #                 font = ImageFont.truetype(fontpath, 200)
    #             img_pil = Image.fromarray(bk_img)
    #             draw = ImageDraw.Draw(img_pil)
    #             # 绘制文字信息
    #             draw.text((1063, 1535),  add_text, font=font,
    #                     fill=(255, 255, 255), anchor="mm",
    #                     align="center")
    #             font = ImageFont.truetype(fontpath, 110)
    #             draw.text((1063, 1300),  conf, font=font,
    #                     fill=(255, 255, 255), anchor="mm",
    #                     align="center")
    #             _img = np.array(img_pil)
    #             cv2.imwrite(conf+'/'+str(idx)+str(i)+".png", _img)
    # else:
    #     add_text = data[conf+' Name']
    #     if len(add_text) > 15:
    #         font = ImageFont.truetype(fontpath, 215-3*len(add_text))
    #     else:
    #         font = ImageFont.truetype(fontpath, 200)
    #     img_pil = Image.fromarray(bk_img)
    #     draw = ImageDraw.Draw(img_pil)
    #     # 绘制文字信息
    #     draw.text((1063, 1535),  add_text, font=font,
    #             fill=(255, 255, 255), anchor="mm",
    #             align="center")
    #     font = ImageFont.truetype(fontpath, 110)
    #     draw.text((1063, 1300),  conf, font=font,
    #             fill=(255, 255, 255), anchor="mm",
    #             align="center")
    #     _img = np.array(img_pil)
    #     cv2.imwrite(conf+'/-'+str(idx)+".png", _img)
    # exit(0)

