from tkinter import *
import calendar



window=Tk()
window.geometry("650x450")
window.title("Calendar")
window.config(background="white")

def show():
    window1=Tk()
    window1.config(background="white")
    window1.title("CALENDAR")
    window1.geometry("550x600")
    year_value=int(year.get())
    c=calendar.calendar(year_value)
    calendar_label=Label(window1,text=c,font=("Consolas 10 bold"))
    calendar_label.grid(row=5,column=1,padx=20)
    


calendar=Label(window,text="CALENDAR",bg="grey",fg="black",font=("Times", 35, "bold"))
calendar.pack(pady=20)

enter_year=Label(window,text="Enter Year",bg="lime",fg="black",font=("Arial",21))
enter_year.place(x=250,y=100)

year=Entry(window,width=15,bg="white",fg="black",font=("Arial",25))
year.place(x=190,y=156)

show_calendar=Button(window,text="Show Calendar",bg="red",fg="black",font=("Arial",15),command=show)
show_calendar.place(x=242,y=216)

exit=Button(window,text="Exit",bg="red",fg="black",font=("Arial",15))
exit.place(x=292,y=276)







window.mainloop()
