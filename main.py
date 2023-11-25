from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#22092C"
COLOR = "#132043"
TIMER_COLOR = "#8ECDDD"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timers = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timers)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=TIMER_COLOR)
    input_text.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    if minutes < 10:
        minutes = f'0{minutes}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if int(minutes) > 0 or int(seconds) > 0:
        global timers
        timers = window.after(1000, count_down,count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✔"
        input_text.config(text=mark)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    #if it is the first, third, fifth or seventh rep:
    if reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)

canvas = Canvas(width=200,height=224, bg=BLUE, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


#Label
timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=BLUE, fg=TIMER_COLOR)
timer.grid(column=1, row=0)

#Start Button
reset_button = Button(text="Start", font=("Arial", 10, "bold"), bg=BLUE, fg=GREEN, command=start_timer)
reset_button.grid(column=0,row=2)

#Reset Button
reset_button = Button(text="Reset", font=("Arial", 10, "bold"), bg=BLUE, fg=RED, command=reset_timer)
reset_button.grid(column=2,row=2)

#Check_mark_label
input_text = Label(text="",font=("Arial", 16, "bold"),bg=BLUE, fg=COLOR)
input_text.grid(column=1,row=3)













window.mainloop()