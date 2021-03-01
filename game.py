### Time Lord Game

from tkinter import *
import time, random
from PIL import ImageTk,Image
from statistics import mean

### variables

level = "easy"
results = []

root=Tk()
root.geometry('625x400+100+100')
root.resizable(width=0, height=0)
root.title("Time Lord")

#Insert Time Lord Image

title_img = ImageTk.PhotoImage(Image.open("timelord_img.jpg"))
title_label = Label(image=title_img)
title_label.grid(row=0,column=0,columnspan=3)

def game_start(difficulty):
	global level
	global time_start
	global time_game
	global var
		
	level = difficulty
	print("level: " + difficulty)
	
	button_easy.grid_forget()
	button_medium.grid_forget()
	button_hard.grid_forget()
	
	if difficulty == "easy":
		time_game = random.randrange(2,10)
	elif difficulty == "medium":
		time_game = random.randrange(11,30)
	else:
		time_game = random.randrange(31,60)
	
	print("game time: " + str(time_game))
	
	
	gt = Label(root, text="Press stop in " + str(time_game) + " seconds", font=("Ariel", 16))
	gt.grid(row=1,column=1)
	
			
	button_cd = Button(root, width=10, font=("Ariel", 16), text="Get ready...", state="disable")
	button_cd.grid(row=2,column=1)
	
	root.update()
	time.sleep(2)

	button_cd.grid_forget()
	button_stop.grid(row=3,column=1)
	
	time_start = time.time()
	print("start time: %f " % time_start)



def level_select():
	button_easy.grid(row=1,column=0)
	button_medium.grid(row=1,column=1)
	button_hard.grid(row=1,column=2)
	
def stop_timer():
	
	global results
	global time_start
	
	time_stop = time.time()
	print("stop time: %f " % time_stop)
	time_length = time_stop - time_start
	print("length of time: %f" % time_length)
	time_score = round(time_game - time_length, 2)
	print("score time: %f" % time_score)

	st = Label(root, text="", font=("Ariel", 16))
	st.grid(row=4,column=1)

	av = Label(root, text="", font=("Ariel", 16))
	av.grid(row=5,column=1)
	
	if time_score > 0:
		over_under = "You were under by " + str(time_score) + " s"
		results.append(time_score)
	elif time_score < 0:
		over_under = "You were over by " + str(-1 * time_score) + " s"
		results.append(-1 * time_score)
	else:
		over_under = "You are spot on!"
		results.append(time_score)
	
	print("results : " + str(results[-1]))	
	print("qty: " + str(len(results)))
	
	average_score = mean(results)
	
	print("average : " + str(average_score))
	
	st.config(text=over_under)
#	st.grid(row=4,column=1)
	
	av.config(text="Your average time is: " + str(round(average_score, 2))+ " s")
	av.grid(row=5,column=1)
	
	time_start = time.time()
	
#	button_stop.grid_forget()
	
#define buttons

button_easy = Button(root, text="Easy", width = 10, font=("Ariel", 16), command=lambda *args: game_start("easy"))
button_medium = Button(root, text="Medium", width = 10, font=("Ariel", 16), command=lambda *args: game_start("medium"))
button_hard = Button(root, text="Hard", width = 10, font=("Ariel", 16), command=lambda *args: game_start("hard"))
button_stop = Button(root, text="Stop", width = 10, font=("Ariel", 16), command=stop_timer)

level_select()

root.mainloop()
