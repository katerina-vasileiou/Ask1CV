import sys
import numpy as np
from PIL import Image

# terminals input-arguments
inputPicName = sys.argv[1]
outputPicName = sys.argv[2]
thdKey = sys.argv[3]

img = Image.open(inputPicName)  # open the image from the given path
pixelsData_array = np.array(img)  # put the given image in a numpy array
width, height = img.size  # keep the image' s size

# check if the opened image is grayscale mode
isGray = True  # set isGray to true, which means the image is grayscale mode
imgNew = img.convert("RGB")  # imgNew is the opened image converted to RGB

for i in range(width):  # traverse the numpy array
    for j in range(height):
        r, g, b = imgNew.getpixel((i, j))  # keep the rgb values of each pixel

        if r != g != b:  # r, g, b aren't equal
            isGray = False  # then the image isn't grayscale
            break
    if isGray == False:
        break

# Convert the image to grayscale mode
if not isGray:  # if the image isn't grayscale
    gray = Image.new("L", (width, height))  # create a new image in greyscale mode with the same size with
                                            # the opened one
    for i in range(width):                  # traverse the new image
        for j in range(height):
            red, green, blue = imgNew.getpixel((i, j))
            newPxl = (red + green + blue) / 3 # at each pixel set the average colour value
            newPxl = int(newPxl)                # convert the value at an int value
            gray.putpixel((i, j), newPxl)       # modifies the pixels at the given position
    image = gray                                # set the graycale converted image at the first one
    pixelsData_array = image.load()             # loads the pixels data from the converted to grayscale image

# Threshold of image
for i in range(width):                          # traverse the image
    for j in range(height):
        if img.getpixel((i, j)) > int(thdKey):  # if the pixel at this position is bigger than given treshold key
            img.putpixel((i, j), 255)           # then set at this pixel the value 255 ( white )
        else:
            img.putpixel((i, j), 0)             # else set it at value 0 ( black )

img.save(outputPicName, format="PNG")           # save the image with the given output name as a png image
img.show()                                      # show the final image
