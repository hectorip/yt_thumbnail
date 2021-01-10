from PIL import ImageColor, Image, ImageDraw, ImageFont
import requests
import datetime
import os

def download_image(keyword="abstract"):
    request = requests.get(
        "https://source.unsplash.com/1600x900/?"+keyword,
        allow_redirects=True
        )
    f = open("images/{}.jpg".format(datetime.datetime.now()), 'wb')
    f.write(request.content)
    return f.name
img = Image.new("RGB", (1280, 720), 'black')
bg_f = download_image()
bg = Image.open(bg_f)
img.paste(bg)
img = Image.eval(img, lambda x: x/2)
d = ImageDraw.Draw(img)
font =  ImageFont.truetype("/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf", 104, encoding="unic")
# d.rectangle(((0,0), (1280, 720)), fill=(0, 0, 0, 120),)
d.text((100, 100), "Hola", fill='white', font=font, )
img.save("t.png")
# img.show()
# os.remove(bg_f)
