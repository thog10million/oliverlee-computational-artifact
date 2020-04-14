
import matplotlib.pyplot as plt
import os.path
import numpy as np      # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, '2c1.jpg')
# Read the image data into an array
img = plt.imread(filename)


'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
# Show the image data in a subplot

ax[0].imshow(img)
ax[1].imshow(img)
ax[2].imshow(img)
ax[3].imshow(img)
ax[4].imshow(img)
# Show the figure on the screen
plt.show()



