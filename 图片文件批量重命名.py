import os
import exifread
from tkinter.filedialog import askdirectory

current_path = askdirectory()
if current_path == " ":
    exit()

all_files = os.listdir(current_path)
images = []
dates = {}

for i in all_files:  # Find all the files that is a picture
    if i[-4:] == ".jpg" or i[-4:] == ".JPG" or i[-5:] == ".jpeg" or i[-4:] == "PNG" or i[-4:] == "png":
        images.append(i)

for i in images:    # Get the date data in each picture and store in a dictionary
    image = current_path + "/" + i
    fd = open(image, "rb")
    tags = exifread.process_file(fd)
    fd.close()
    for tag in tags:
        if tag == "Image DateTime":
            dates.update({str(tags[tag])[0:10]: 1})

for i in images:
    image = current_path + "/" + i
    fd = open(image, "rb")
    tags = exifread.process_file(fd)
    fd.close()
    for tag in tags:
        if tag == "Image DateTime":
            date = str(tags[tag])[0:10]
    new_name = str(date) + "-" + str(dates[date]) + ".jpg"
    dates.update({date: dates[date] + 1})
    os.rename(image, current_path + "/" + new_name)
