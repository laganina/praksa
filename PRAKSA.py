from PIL import Image
from glob import glob
import os

# loading images
image_paths = glob(os.getcwd() + '/input/*.png')

images = []
for path in image_paths:
    image = Image.open(path)
    images.append(image)

# defining the size of the new image
width = images[0].width
height = images[0].height

# creating new image
new_image = Image.new('RGB', (width, height))

# iterating over rows
n = 0
while n < height + 1:
    max_width = max(image.width for image in images)
    new_image = Image.new('RGB', (width, len(images)))

    for i, image in enumerate(images):
        if n < image.height + 1:
            row = image.crop((0, n, image.width, n+1))
            new_image.paste(row, (0, i))

    new_image.save(f'output/row_{n}.png')
    n += 1

# iterating over columns
n = 0
while n < width + 1:
    max_height = max(image.height for image in images)
    new_image = Image.new('RGB', (len(images), height))

    for i, image in enumerate(images):
        if n < image.width + 1:
            column = image.crop((n, 0, n+1, image.height))
            new_image.paste(column, (i, 0))

    new_image = new_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    new_image.save(f'output/column_{n}.png')
    n += 1