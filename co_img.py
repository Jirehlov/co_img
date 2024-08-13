import os
from PIL import Image
sub_height = 120
def resize_image(image, target_width):
    ratio = target_width / image.width
    resized_image = image.resize((int(image.width * ratio), int(image.height * ratio)))
    return resized_image
def concatenate_images(output_path):
    image_files = [file for file in os.listdir() if file.endswith('.png')]
    image_files.sort()
    first_image = resize_image(Image.open(image_files[0]), 1920)
    width, height = first_image.size
    total_height = height + (len(image_files) - 1) * sub_height
    new_image = Image.new('RGB', (1920, total_height))
    new_image.paste(first_image, (0, 0))
    offset = height
    for index, image_file in enumerate(image_files[1:]):
        img = resize_image(Image.open(image_file), 1920)
        cropped_img = img.crop((0, img.height - sub_height, img.width, img.height))
        new_image.paste(cropped_img, (0, offset))
        offset += sub_height
    new_image.save(output_path)
output_path = 'out.png'
concatenate_images(output_path)
