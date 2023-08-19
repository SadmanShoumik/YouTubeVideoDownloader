from pytube import YouTube

while 1:
    link = input("Enter Video Link (Press q to Quit): ")

    if link == "q":
        break

    yt = YouTube(link)

    print("\nTitle: ", yt.title)
    print("Length:", yt.length // 60, "m", yt.length % 60, "s")

    ydown = yt.streams.get_highest_resolution()
    print("Video Size: ", ydown.filesize_mb, "mb")
    print("Video Resolution: ", ydown.resolution)

    s = input("Do You Wish to Download this Video? (y/n) ---> ")
    if s == "y":
        ydown.download('D:/Downloads')
        print("Download Completed!\n\n")
    else:
        continue

# Demo Link to Try Out the Program
# https://www.youtube.com/watch?app=desktop&v=10hBPggOaD8&t=0s
