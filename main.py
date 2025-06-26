import tkinter as tk
import fnmatch
import os
from pygame import mixer

os.chdir(os.path.dirname(os.path.abspath(__file__)))

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg="black")

rootpath = "C:\\Users\\sudey\\OneDrive\\Belgeler\\music"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="prev_img.png")
play_img = tk.PhotoImage(file="play_img.png")
pause_img = tk.PhotoImage(file="pause_img.png")
stop_img = tk.PhotoImage(file="stop_img.png")
next_img = tk.PhotoImage(file="next_img.png")


images = [prev_img, play_img, pause_img, stop_img, next_img]

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    if next_song:
        next_index = next_song[0] + 1
        if next_index < listBox.size():
            next_song_name = listBox.get(next_index)
            label.config(text=next_song_name)

            mixer.music.load(rootpath + "\\" + next_song_name)
            mixer.music.play()

            listBox.select_clear(0, 'end')
            listBox.activate(next_index)
            listBox.select_set(next_index)

def play_prev():
    prev_song = listBox.curselection()
    if prev_song:
        prev_index = prev_song[0] - 1
        if prev_index >= 0:
            prev_song_name = listBox.get(prev_index)
            label.config(text=prev_song_name)

            mixer.music.load(rootpath + "\\" + prev_song_name)
            mixer.music.play()

            listBox.select_clear(0, 'end')
            listBox.activate(prev_index)
            listBox.select_set(prev_index)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('poppins', 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text="", bg='black', fg='yellow', font=('poppins', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor="center")

prevButton = tk.Button(canvas, image=prev_img, borderwidth=0, command=play_prev,background="black")
prevButton.pack(pady=15, in_=top, side="left")

stopButton = tk.Button(canvas, image=stop_img, borderwidth=0, command=stop,background="black")
stopButton.pack(pady=15, in_=top, side="left")

playButton = tk.Button(canvas, image=play_img, borderwidth=0, command=select, background="black")
playButton.pack(pady=15, in_=top, side="left")

pauseButton = tk.Button(canvas, image=pause_img, borderwidth=0, command=pause_song, text="Pause",  background="black")
pauseButton.pack(pady=15, in_=top, side="left")

nextButton = tk.Button(canvas, image=next_img, borderwidth=0, command=play_next, background="black")
nextButton.pack(pady=15, in_=top, side="left")

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()


