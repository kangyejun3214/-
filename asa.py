import tkinter as tk
def startTimer():
    if (running):
        global timer
        timer += 1
        timeText.configure(text= f'{timer/100:.2f} s')
    window.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

def initial():
    global running
    running = False
    global timer
    timer = 0
    timeText.configure(text= f'{timer/100:.2f} s')

running = False
# initialing = True
window = tk.Tk()
window.geometry('400x200')
timer = 0

timeText = tk.Label(window, text = '0', font=("Helvetica", 80))
timeText.pack()

startButton = tk.Button(window, text = 'Start', bg='yellow', command=start)
startButton.pack(fill=tk.BOTH)

stopButton = tk.Button(window, text = 'Stop', bg='red', command=stop)
stopButton.pack(fill=tk.BOTH)

initialButton = tk.Button(window, text = 'Initial', bg='green', command=initial)
initialButton.pack(fill=tk.BOTH)

startTimer()

window.mainloop()