import cv2
import imageio
import os
from pathlib import Path
import time


def video_to_frames(filelocation):  # a function that selects an mp4 file that will convert it into images.
    print(filelocation)
    print("Converting MP4 to Frames...")

    mp4file = cv2.VideoCapture(filelocation)
    num = 0

    filename = filelocation.split('\\')[-1].replace('.mp4', '')
    file_folder = os.getcwd() + f"\\imgs\\{filename}\\"
    os.mkdir(file_folder)
    path = file_folder + "image_{}"

    while mp4file.isOpened():  # Checks if mp4File is still running.
        print("Doing Something")
        ret, frame = mp4file.read()
        if ret == False:
            break
        cv2.imwrite(path.format(str(num)) + '.jpg', frame)
        num += 1

    mp4file.release()
    cv2.destroyAllWindows()
    print("Images Saved...\n----------------------------")
    return filename


def images_to_gif(filename):
    print("Converting Images To GIF...")
    paths = sorted(Path(os.getcwd() + f"//imgs//{filename}//").iterdir(), key=os.path.getmtime)
    images = []
    print("Creating GIF...")
    for each_image in paths:
        images.append(imageio.imread(each_image))
    output = "gifs/" + filename + ".gif"
    imageio.mimsave(output, images, fps=30)  # fps var can be changed to 15, 24, 60
    print("GIF Created!")


def dir_check():
    dirList = ["imgs", "gifs", "vid"]
    print("Initial Check...\nchecking missing folders...")

    for dir in dirList:
        if dir not in os.listdir():
            os.mkdir(os.getcwd() + f"//{dir}...")
            print(f"creating {dir} folder")
    else:
        print("Done...\n---------------------------- ")


def user_input():
    print("File Available: {Select the number you want to use or path from directory}")
    vid_list = os.listdir(os.getcwd() + "//vid")
    [print(f"{files} - {vid_list.index(files) + 1}") for files in vid_list] if len(vid_list) != 0 else print(
        "No Files Available")

    while True:
        user_in = input("File: ")
        user_bool = user_in.isnumeric()
        if user_bool:
            if 0 < int(user_in) <= len(vid_list):
                print("----------------------------")
                return os.getcwd() + f"\\vid\\{vid_list[int(user_in) - 1]}"

            else:
                print("Number should be listed above. Try Again.")
        else:
            if os.path.exists(user_in):
                print("----------------------------")
                return user_in

            else:
                print("Invalid File Path. Try Again")

dir_check()
filename = video_to_frames(user_input())
time.sleep(5)
images_to_gif(filename)

