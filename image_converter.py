from PIL import Image
from pathlib import Path
from os import listdir, remove


x = Path().cwd()
files = [y for y in listdir(x) if y.endswith('.webp')]
for file in files:
    old_image = x / file
    new_image = x / f'{file[:-5]}.png'
    im = Image.open(old_image)
    im.save(new_image, format='png', lossless=True)
    remove(old_image)
