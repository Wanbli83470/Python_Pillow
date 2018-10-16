from PIL import Image, ImageFilter
import os
#Turn image 
image1 = Image.open("Gobelin.png")
image1.rotate(90).save("Gobelin_rotate.png")
image1.show()

#Black and white
image1.convert(mode = 'L').save("Gobelin_Black_white.png")

#Filter
image1.filter(ImageFilter.GaussianBlur(4)).save("Gobelin_blur.png")