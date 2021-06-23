from console.utils import set_title
from PIL import Image
import random
import os

__version__ = '1.0.5-beta'
__author__ = 'Baziki#7133'

ASCII_CHARS = "@#S%?*+;:,. "
ASCII_WIDTH = 80  # terminal width

TITLE = """
.d8b.  .d8888.  .o88b. d888888b d888888b       .d8b.  d8888b. d888888b      d888888b  .d88b.   .d88b.  db      
d8' `8b 88'  YP d8P  Y8   `88'     `88'        d8' `8b 88  `8D `~~88~~'      `~~88~~' .8P  Y8. .8P  Y8. 88      
88ooo88 `8bo.   8P         88       88         88ooo88 88oobY'    88            88    88    88 88    88 88      
88~~~88   `Y8b. 8b         88       88         88~~~88 88`8b      88            88    88    88 88    88 88      
88   88 db   8D Y8b  d8   .88.     .88.        88   88 88 `88.    88            88    `8b  d8' `8b  d8' 88booo. 
YP   YP `8888Y'  `Y88P' Y888888P Y888888P      YP   YP 88   YD    YP            YP     `Y88P'   `Y88P'  Y88888P
"""


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def resize_image(image, new_width=ASCII_WIDTH):
    """Resize image according to a new width."""
    width, height = image.size
    new_height = int((height / width) * new_width * 0.55)
    return image.resize((new_width, new_height))


def pixel_to_ascii(image):
    """Convert pixels to a string of ascii characters"""
    return ''.join(ASCII_CHARS[int((pixel / 256) * len(ASCII_CHARS))] for pixel in image.getdata())


def main():
    set_title(f'ASCII Art Convert - v{__version__} | by {__author__}')
    os.system('cls')

    print(TITLE)
    print(f"\nAuthor: {__author__}")
    is_running = True

    while is_running:
        path = input("#if you want to exit type 'exit' or 'quit'\nImage Patch: ")

        if path in ['exit', 'quit', 'EXIT', 'QUIT']:
            is_running = False

        if not os.path.exists(path):
            print(path, "is not a valid path.")
            continue

        image = Image.open(path)

        print("Converting your image to ASCII....")
        new_image_data = pixel_to_ascii(resize_image(image).convert("L"))

        print("Your ASCII Image:")
        print('\n'.join(chunks(new_image_data, ASCII_WIDTH)))

        print("Your ASCII image has been saved to image.txt")
        os.system("pause")

        with open("image.txt", "w+") as f:
            f.write(ascii_image)

    print("Exiting....")


if __name__ == '__main__':
    main()
