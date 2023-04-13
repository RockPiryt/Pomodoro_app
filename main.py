from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # global variable to work/break system
timer = None# global variable to reset_timer function
#zmienna timer zaczyna jako None aby potem w pętli window.after zmienić wartość

# ---------------------------- TIMER RESET ------------------------------- # 
#Function make:
#---stop the timer
#---reset text in timer,
#---reset checkmark
#---reset title_label to Timer
#---reset reps

def reset_timer():
    #stop timer
    window.after_cancel(timer)#do zamknięcia pętli after, która odlicza
    #---reset text in timer,
    canvas.itemconfig(timer_text, text='00:00')
    #---reset checkmark
    check_mark.config(text = ' ')
    #---reset title_label to Timer
    timer_label.config(text='Timer')

    #reset reps
    #aby zaczynać od WORK a nie BREAK
    global reps
    reps = 0 #wyzerowanie powtórzeń gdy reset zegara, bo liczba powtórzeń stale rośnie






# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    #work/break system
    global reps #repetitions
    reps += 1 #zwiększanie cyfry powtórzeń - nowa pętla uruchomina poprzez funkcję start timer

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #if it's the 8 rep (powtorzenie) --->LONG_BREAK
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config( text='Long break', fg=RED)
    elif reps % 2 == 0: #parzyste powtórzenia
        #if it's the 2/4/6 rep (powtorzenie) --->SHORT_BREAK
        count_down(short_break_sec)
        timer_label.config( text='Short break', fg=PINK)
    else:
    #if it's the 1/3/5/7 rep (powtorzenie) --->WORK
        count_down(work_sec)
        timer_label.config( text='Work', fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

#method 1 not working in tkinter - window.loop
# import time

# count = 5

# while True:
#     time.sleep(-1)
#     count -= 1

#method 2 - metoda after z tkinter
def count_down(count):
    #"04:05"
    # 245 / 60 =4.05 divide by seconds
    # 245 % 60=5 modulo
    # jeżeli 240/60 wtedy remainder to 0 a nie 00

    count_min = math.floor(count / 60) #we don't want 3,6 - math.floor() return largest whole number or equal to x- 
    #it return 4 min

    count_sec = count % 60 # return reminder number - 5 seconds

    # jeżeli 240/60 wtedy remainder to 0 a nie 00
    #przykład dynamic typing - zmiana typu zmiennej
    # if count_sec == 0:# to nie wyświetli 00:09
    #     count_sec == "00"

    if count_sec < 10:#to doda zero przed cyframi, wyświetli 00:09
        count_sec = f"0{count_sec}"#przypisanie do zmiennej



    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')#napis licznika
    if count > 0:#WARUNEK jeżeli warunek jest spełniony to wykonuj funkcje, w przeciwnym wypadku zaprzestań
        global timer#poza funkcją utworzono zmienną globalną - tutaj ją wywołuje (na początek ma wartość None)
        timer = window.after(1000, count_down, count-1)#PĘTLA do odliczania, zmienia wartość timer z None
        #przypisanie do zmiennej timer (jest to zmienna lokalna użyta w funkcji)
        # muszę ją wyciągnąc poza funkcję(zrobić zmienną globalną)

    else:
        start_timer()#uruchomienie kolejnego powtórzenia po dojsci zegara do zera
        
        
        #add checkmarks after each 2 reps (work+break)
        marks = ' '
        #math.floor for whole number - reps/2=float, range only whole number
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += '✔'
        check_mark.config(text=marks)# after each for_loop update checkmark




# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title('Pomodoro countdown')
window.config(padx=200, pady=120, bg=YELLOW)
# count_down(5)

# def say_something(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# window.after(1000, say_something, 3, 5, 8)#po okreslonej ilosci milisekund, wywolywana jest funkcja i przekazane są argumenty
# #można przekazać wiele argumentów
# #po 1 sekundzie wyświtlą sie wszystkie trzy cyfry

canvas = Canvas(width=500, height=224, bg=YELLOW, highlightthickness=0)#create canvas, value like img
tomato_img = PhotoImage(file="tomato.png")#variable for img file
canvas.create_image(250,112, image=tomato_img)#init method - x,y position of image's center and variable for photo img

#variable timer_text for loop - window.after()
timer_text =canvas.create_text(250,130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))#text on above image!!! - canvas.create_text
#init method - x,y position of text center
canvas.grid(column=1, row=1)

# count_down(5)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text=' ', fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=2)


window.mainloop()
