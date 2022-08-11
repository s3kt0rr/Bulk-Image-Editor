from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathout = '/finalPosts'

for filename in os.listdir((path)):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).rotate(-90)

    factor = 2.5
    enhancer = ImageEnhance.Color(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathout}/{clean_name}_edited.jpg')

