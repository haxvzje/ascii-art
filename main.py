from console.utils import set_title
from PIL import Image
import random
import time
from os import system

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pta(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # attempt to open image from user-input
    print(logo + f"\nAuthor: {author}")
    print(f"Session: {se1}{se2}{se3}{se4}\n")
    while True:
	    path = input("#if you want to exit type 'exit' or 'quit'\nImage Patch: ")
	    if path=='exit' or path=='quit' or path=='EXIT' or path=='QUIT':
	    	print("\nExiting....")
	    	time.sleep(3)
	    	exit()
	    try:
	        image = Image.open(path)
	        break
	    except:
	        print(path, "is not a valid path.")
	        pass
  
    # convert image to ascii
    print("\nConverting your image to ASCII....")
    time.sleep(3)
    new_image_data = pta(grayify(resize_image(image)))
    
    # format
    print("\nFormat your ASCII image....")
    time.sleep(2)
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print("\nYour ASCII Image:")
    print(ascii_image)
    print("\nYour ASCII image has been saved to 'image.txt'")
    input()
    
    # save result to "image.txt"
    with open("image.txt", "w") as f:
        f.write(ascii_image)
 
# run program
if __name__ == '__main__':
	logo = ''' .d8b.  .d8888.  .o88b. d888888b d888888b       .d8b.  d8888b. d888888b      d888888b  .d88b.   .d88b.  db      
d8' `8b 88'  YP d8P  Y8   `88'     `88'        d8' `8b 88  `8D `~~88~~'      `~~88~~' .8P  Y8. .8P  Y8. 88      
88ooo88 `8bo.   8P         88       88         88ooo88 88oobY'    88            88    88    88 88    88 88      
88~~~88   `Y8b. 8b         88       88         88~~~88 88`8b      88            88    88    88 88    88 88      
88   88 db   8D Y8b  d8   .88.     .88.        88   88 88 `88.    88            88    `8b  d8' `8b  d8' 88booo. 
YP   YP `8888Y'  `Y88P' Y888888P Y888888P      YP   YP 88   YD    YP            YP     `Y88P'   `Y88P'  Y88888P '''
	version = '1.0.5-beta'
	author = 'Baziki#7133'
	se1 = random.randint(0,9)
	se2 = random.randint(0,9)
	se3 = random.randint(0,9)
	se4 = random.randint(0,9)

	set_title(f'ASCII Art Convert - v{version} | by {author}')
	system('cls')
	main()