# MemeMaker
A program that adjust few or many lines of text into an image to create a meme.
It can add up to 7 legible lines of text distributed up and down.

##Make a meme
Only three parameters.
Markup: *A jpg image
        *Text
        *A font
    
##Demo    
<!--code-->
```python
from MemeMaker import memefy
fontdir="/System/Library/Fonts/Supplemental/Impact.ttf"  #MacOS
text="Lorem ipsum dolor sit amet, consectetur adipiscin"
img=memefy("doge.jpg",txt, fontdir)
img.save("superdoge.jpg")
```
