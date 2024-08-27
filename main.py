import tkinter
from tkinter import Entry, Label


def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.6094, 2)
        calculation_label.config(text=km)
    except ValueError:
        calculation_label.config(text='Oops!')


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(0, "0")
miles_input.grid(column=1, row=0)

mile_label = Label(text='Miles')
mile_label.grid(column=2, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

calculation_label = Label(text='0')
calculation_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
