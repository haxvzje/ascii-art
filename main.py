from console.utils import set_title
from PIL import Image
import random
import os

__version__ = '1.0.5-beta'
__author__ = 'Baziki#7133'


# ascii characters used to build the output text
ASCII_CHARS = "@#S%?*+;:,."

TITLE = """
.d8b.  .d8888.  .o88b. d888888b d888888b       .d8b.  d8888b. d888888b      d888888b  .d88b.   .d88b.  db      
d8' `8b 88'  YP d8P  Y8   `88'     `88'        d8' `8b 88  `8D `~~88~~'      `~~88~~' .8P  Y8. .8P  Y8. 88      
88ooo88 `8bo.   8P         88       88         88ooo88 88oobY'    88            88    88    88 88    88 88      
88~~~88   `Y8b. 8b         88       88         88~~~88 88`8b      88            88    88    88 88    88 88      
88   88 db   8D Y8b  d8   .88.     .88.        88   88 88 `88.    88            88    `8b  d8' `8b  d8' 88booo. 
YP   YP `8888Y'  `Y88P' Y888888P Y888888P      YP   YP 88   YD    YP            YP     `Y88P'   `Y88P'  Y88888P
"""


# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width * 0.55)
    return image.resize((new_width, new_height))


# convert each pixel to grayscale
def gray_ify(image):
    return image.convert("L")


# convert pixels to a string of ascii characters
def pta(image):
    return ''.join(ASCII_CHARS[pixel // 25] for pixel in image.getdata())


def main():
    set_title(f'ASCII Art Convert - v{__version__} | by {__author__}')
    os.system('cls')

    # attempt to open image from user-input
    print(TITLE)
    print(f"\nAuthor: {__author__}")
    print(f"Session: {random.randint(0, 9999):04}\n")

    is_running = True

    while is_running:
        path = input("#if you want to exit type 'exit' or 'quit'\nImage Patch: ")

        if path in ['exit', 'quit', 'EXIT', 'QUIT']:
            print("\nExiting....")
            is_running = False

        if not os.path.exists(path):
            print(path, "is not a valid path.")
            continue

        image = Image.open(path)
        convert_image(image)


def convert_image(image, new_width=100):
    # convert image to ascii
    print("\nConverting your image to ASCII....")
    new_image_data = pta(gray_ify(resize_image(image)))

    # format
    print("\nFormat your ASCII image....")

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[index: (index + new_width)] for index in range(0, pixel_count, new_width))

    # print result
    print("\nYour ASCII Image:")
    print(ascii_image)
    print("\nYour ASCII image has been saved to 'image.txt'")
    os.system("pause")

    # save result to "image.txt"
    with open("image.txt", "w") as f:
        f.write(ascii_image)


# run program
if __name__ == '__main__':
    main()
