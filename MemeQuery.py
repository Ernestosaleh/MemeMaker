from MemeMaker import memefy
from lorem_text import lorem

font="/System/Library/Fonts/Supplemental/Impact.ttf"  #MacOS
#Windows?

txt=lorem.paragraphs(3)[0:50]
img=memefy("doge.jpg",txt, font)
img.save("superdoge.jpg")
