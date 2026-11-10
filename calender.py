from tkinter import *


window=Tk()
window.geometry("650x450")
window.title("Calendar")
window.config(background="white")

calendar=Label(window,text="CALENDAR",bg="grey",fg="black",font=("Times", 35, "bold"))
calendar.pack(pady=20)

enter_year=Label(window,text="Enter Year",bg="lime",fg="black",font=("Arial",21))
enter_year.place(x=250,y=79)

year=Entry(window,width=10,bg="")



window.mainloop()