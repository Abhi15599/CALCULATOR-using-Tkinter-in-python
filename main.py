from tkinter import *
from tkinter import messagebox


val = ""
A = 0
operator = ""

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)


def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)


def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)


def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)


def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)


def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)


def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)


def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)


def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


def btnplus_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btnminus_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btnmultiply_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btndiv_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btnclear_isclicked():
    global val
    global A
    global operator
    val = ""
    A = 0
    data.set(val)


def result():
    global val
    global A
    global operator
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("error", "number cannot be divisible by 0")
            val = ""
            A = ""
            data.set(val)
        C = int(A / x)
        data.set(C)
        val = str(C)



root = Tk()
root.title("CAlculator")
root.geometry("250x400+300+300")

data = StringVar()
lbl = Label(
    root,
    text="input here!",
    anchor=SE,
    font=("verdana", 22),
    textvariable=data,
    bg="#ffffff",
    fg="#000000"
)
lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root, )
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

# val = ""
# def btn_1_clicked():
#     global val
#     val = val + "1"
#     data.set(val)
# def btn_2_clicked():
#     global val
#     val = val+"2"
#     data.set(val)


btn1 = Button(
    btnrow1,
    text="1",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,
)

btn1.pack(expand=True, side=LEFT, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn2.pack(expand=True, side=LEFT, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn3.pack(expand=True, side=LEFT, fill="both")

btnplus = Button(
    btnrow1,
    text="+",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btnplus_clicked,
)
btnplus.pack(expand=True, side=LEFT, fill="both")

# for btnrow2
btn4 = Button(
    btnrow2,
    text="4",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked,
)
btn4.pack(expand=True, side=LEFT, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,
)
btn5.pack(expand=True, side=LEFT, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,

)
btn6.pack(expand=True, side=LEFT, fill="both")

btnminus = Button(
    btnrow2,
    text="- ",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btnminus_clicked,
)
btnminus.pack(expand=True, side=LEFT, fill="both")

# for buttonrow3
btn7 = Button(
    btnrow3,
    text="7",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked,

)
btn7.pack(expand=True, side=LEFT, fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked,

)
btn8.pack(expand=True, side=LEFT, fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,

)
btn9.pack(expand=True, side=LEFT, fill="both")

btnmultiply = Button(
    btnrow3,
    text="* ",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btnmultiply_clicked,
)
btnmultiply.pack(expand=True, side=LEFT, fill="both")

# for buttonrow4
btnclear = Button(
    btnrow4,
    text="C",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command = btnclear_isclicked,
)
btnclear.pack(expand=True, side=LEFT, fill="both")

btn0 = Button(
    btnrow4,
    text="0",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_0_isclicked,
)
btn0.pack(expand=True, side=LEFT, fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command = result,
)
btnequal.pack(expand=True, side=LEFT, fill="both")

btndiv = Button(
    btnrow4,
    text="/ ",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btndiv_clicked,
)
btndiv.pack(expand=True, side=LEFT, fill="both")

root.mainloop()
