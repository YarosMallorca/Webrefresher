import keyboard
import time
from selenium import webdriver
from tkinter import filedialog
from tkinter import *
from tkinter import ttk as ttk
from PIL import Image, ImageTk
import threading
import sys

window = Tk()
window.title("Webrefresher")
window.iconbitmap("Assets/icon.ico")
window.configure(background="white")

window_width = 800
window_height = 350

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

path_already_loaded = False

run = False

def openwebsite():
	global run
	global driver
	global stopbutton
	run = True
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get(html_path)
	startbutton.place_forget()
	stopbutton = ttk.Button(text="Stop html file", command=stopselenium)
	stopbutton.place(x=680, y=170)
	while run:
		if keyboard.is_pressed('Ctrl'):
			if keyboard.is_pressed('s'):
				driver.refresh()
			elif keyboard.is_pressed('q'):
				driver.quit()
				stopbutton.place_forget()
				startbutton.place(x=680, y=170)
				run = False
				break
		time.sleep(0.1)


def stopselenium():
	global run
	if run:	
		driver.quit()
		stopbutton.place_forget()
		startbutton.place(x=680, y=170)
		run = False

def close_window():
	global run
	if run:	
		driver.quit()
		stopbutton.place_forget()
		startbutton.place(x=680, y=170)
		run = False
	window.destroy()
	sys.exit()

def selecthtml():
	global path_already_loaded
	global path_label
	global html_path
	global startbutton
	html_path = filedialog.askopenfilename(title='Choose a song to play',
										   filetypes=(('html files', '*.html'), ('all files', '*')))
	if path_already_loaded:
		path_label.place_forget()

	path_label = Label(text=html_path, font=("Segoe UI", 12), background="white")
	path_label.place(x=125, y=168)
	path_already_loaded = True

	startbutton = ttk.Button(text="Start html file", command=threading.Thread(target=openwebsite).start)
	startbutton.place(x=680, y=170)

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = Image.open("Assets/title.png").resize((540, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

Label(window, image=img, background="white").place(x=130, y=20)
Label(window, text="Select an html file, click open! It will automatically reload when clicking Ctrl + S in any window!", font=("Segoe UI", 12), background="white").place(x=50, y=130)

ttk.Button(text="Open html file", command=selecthtml).place(x=30, y=170)

window.protocol("WM_DELETE_WINDOW", close_window)
window.mainloop()
