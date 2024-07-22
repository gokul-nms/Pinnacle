from tkinter import *

win = Tk() 
win.geometry("312x324")  
win.resizable(0, 0) 

win.title("PINNACLE CALCULATOR")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

def bt_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
 
expression = ""
input_text = StringVar()
 
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="blUE", highlightcolor="blUE", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
 
input_field = Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=50, bg="white", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=15) 

 
button_fr = Frame(win, width=312, height=272.5, bg="darkblue")
 
button_fr.pack()
 
#FIRST ROW IN PINNACLE CALC
 
clear = Button(button_fr, text = "C", fg = "#800080", width = 32, height = 3, bd = 0, bg = "#FFEFD5", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(button_fr, text = "/", fg = "#800080", width = 10, height = 3, bd = 0, bg = "#FFEFD5", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# SECOND ROW IN PINNACLE CALC
 
seven = Button(button_fr, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(button_fr, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(button_fr, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(button_fr, text = "*", fg = "#800080", width = 10, height = 3, bd = 0, bg = "#FFEFD5", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
#   THIRD ROW IN PINNACLE CALC
 
four = Button(button_fr, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(button_fr, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(button_fr, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(button_fr, text = "-", fg = "#800080", width = 10, height = 3, bd = 0, bg = "#FFEFD5", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# FOURTH ROW IN PINNACLE CALC
 
one = Button(button_fr, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(button_fr, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(button_fr, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(button_fr, text = "+", fg = "#800080", width = 10, height = 3, bd = 0, bg = "#FFEFD5", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# FIFTH ROW IN PINNACLE CALC
 
zero = Button(button_fr, text = "0", fg = "white", width = 21, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(button_fr, text = ".", fg = "#800080", width = 10, height = 3, bd = 0, bg = "#FFEFD5", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(button_fr, text = "=", fg = "#800080", width = 10, height = 3, bd = 0, bg = "#FFEFD5", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()