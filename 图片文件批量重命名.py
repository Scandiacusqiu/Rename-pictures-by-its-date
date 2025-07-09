import os
import exifread
from tqdm import tqdm
from tkinter.filedialog import askdirectory

current_path = askdirectory()
if current_path == " ":
    exit()

all_files = os.listdir(current_path)
images = []
types = []
dates = {}

for i in all_files:  # Find all the files that is a picture
    if i[-4:] == ".jpg" or i[-4:] == ".JPG" or i[-4:] == ".PNG" or i[-4:] == ".png" or i[-4:] == ".ARW":
        images.append(i)
        types.append(i[-4:])
    elif i[-5:] == ".jpeg":
        images.append(i)
        types.append(i[-5:])

file_number = len(images)
proceed = input(str(file_number) + ' files detected, proceed? (y/n): ')

if proceed == 'y':
    print('extracting file dates...')
    pbar = tqdm(total=file_number)
    for i in images:    # Get the date data in each picture and store in a dictionary
        image = current_path + "/" + i
        fd = open(image, "rb")
        tags = exifread.process_file(fd)
        fd.close()
        for tag in tags:
            if tag == "Image DateTime":
                dates.update({str(tags[tag])[0:10]: 1})
        pbar.update(1)
    # pbar.close()
    del pbar

    print('dates all extracted')

    print('renaming...')
    pbar = tqdm(total=file_number)
    index = 0
    for i in images:
        image = current_path + "/" + i
        fd = open(image, "rb")
        tags = exifread.process_file(fd)
        fd.close()
        for tag in tags:
            if tag == "Image DateTime":
                date = str(tags[tag])[0:10]
        new_name = str(date) + " " + str(dates[date]) + types[index]
        index += 1
        dates.update({date: dates[date] + 1})
        os.rename(image, current_path + "/" + new_name)
        pbar.update(1)
    pbar.close()
else:
    print("executing")
    exit()
