from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

win = Tk()
win.title('Registartion Univer')
win.geometry('1125x790+100+10')
win.config(bg='gold')

# +++++++++++ project name +++++++++++
univ_name = Label(win, text='Student Registration Form', font=('Times', 20, 'bold'), fg='gold', bg='black',
            bd=10, relief=GROOVE)
univ_name.pack(side=TOP, fill=X)

def subm():
    inf_text.insert(END, f'\t Your information here:')
    inf_text.insert(END, f'\n {(fname.get())}\n {(sname.get())}\n {(fathname.get())}')
    inf_text.insert(END, f'\n {(combo1.get())}\n {(combo2.get())}\n {(combo3.get())}')
    inf_text.insert(END, f'\n {(combo4.get())}\n {(combo5.get())}\n {(combo6.get())}')
    inf_text.insert(END, f'\n {(e_mail.get())}\n {(e_tel.get())}\n')

def clear():
    fname.delete(0, 'end')
    sname.delete(0, 'end')
    fathname.delete(0, 'end')
    combo1.delete(0, 'end')
    combo2.delete(0, 'end')
    combo3.delete(0, 'end')
    combo4.delete(0, 'end')
    e_mail.delete(0, 'end')
    e_tel.delete(0, 'end')

# +++++++++++ all frame ++++++++++++
reg_frame = LabelFrame(win, text='University Registration form', font=('Times', 14),
                       fg='darkred', bg='Lightblue', bd=6, relief=GROOVE)
reg_frame.place(x=15, y=60, width=435, height=540)

campus_frame = LabelFrame(win, text='University Campus', font=('Times', 14),
                          fg='darkred', bg='Lightblue', bd=6, relief=GROOVE)
campus_frame.place(x=460, y=60, width=655, height=540)


img = Image.open('univ_foto/berk2.jpg')
img = img.resize((630, 500), Image.BILINEAR) #, Image.ANTIALIAS
photoimg = ImageTk.PhotoImage(img)

lbl_img_mini = Label(campus_frame, image=photoimg, bd=4, relief=RIDGE)
lbl_img_mini.place(x=2, y=0)

inf_frame = LabelFrame(win, text='Information', font=('Times', 14), fg='darkred',
                       bg='Lightblue', bd=6, relief=GROOVE)
inf_frame.place(x=460, y=600, width=655, height=175)

pic_frame = LabelFrame(win, bg='Lightblue', bd=6, relief=GROOVE)
pic_frame.place(x=15, y=600, width=435, height=175)


icon = Image.open('univ_foto/berk_logo.jpg')
icon = icon.resize((420,160), Image.BILINEAR) #, Image.ANTIALIAS
photoicon = ImageTk.PhotoImage(icon)

lbl_img_mini = Label(pic_frame, image=photoicon, bd=4, relief=RIDGE)
lbl_img_mini.place(x=0, y=0, width=425, height=165)


# +++++++++++ registr. labels +++++++
name = Label(reg_frame, text='Name', font=('Times', 18), fg='darkred', bg='Lightblue')
fname = Entry(reg_frame, font=('Times', 18), fg='darkred')
surname = Label(reg_frame, text='Surname', font=('Times', 18), fg='darkred', bg='Lightblue')
sname = Entry(reg_frame, font=('Times', 18), fg='darkred')
fath_name = Label(reg_frame, text='Father Name', font=('Times', 18), fg='darkred', bg='Lightblue')
fathname = Entry(reg_frame, font=('Times', 18), fg='darkred')
date = Label(reg_frame, text='Date of Birth', font=('Times', 18), fg='darkred', bg='Lightblue')
gen = Label(reg_frame, text='Gender', font=('Times', 18), fg='darkred', bg='Lightblue')
countr = Label(reg_frame, text='Country', font=('Times', 18), fg='darkred', bg='Lightblue')
cit = Label(reg_frame, text='City', font=('Times', 18), fg='darkred', bg='Lightblue')
mail = Label(reg_frame, text='E-mail', font=('Times', 18), fg='darkred', bg='Lightblue')
e_mail = Entry(reg_frame, font=('Times', 18), fg='darkred')
tel = Label(reg_frame, text='Mobile', font=('Times', 18), fg='darkred', bg='Lightblue')
e_tel = Entry(reg_frame, font=('Times', 18), fg='darkred')

name.grid(row=0, column=0, padx=6, pady=4)
fname.grid(row=0, column=1, padx=6, pady=4)
surname.grid(row=1, column=0, padx=6, pady=4)
sname.grid(row=1, column=1, padx=6, pady=4)
fath_name.grid(row=2, column=0, padx=6, pady=4)
fathname.grid(row=2, column=1, padx=6, pady=4)
date.grid(row=3, column=0, padx=6, pady=4)
gen.grid(row=6, column=0, padx=6, pady=4)
countr.grid(row=7, column=0, padx=6, pady=4)
cit.grid(row=8, column=0, padx=6, pady=4)
mail.grid(row=9, column=0, padx=6, pady=4)
e_mail.grid(row=9, column=1, padx=6, pady=4)
tel.grid(row=10, column=0, padx=6, pady=4)
e_tel.grid(row=10, column=1, padx=6, pady=4)

# --------- regstr. combs -------
month = ('January', 'February', 'Mart', 'April', 'May', 'June', 'July', 'August', 'September',
         'October', 'November', 'December')
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
gender = ('Ayal', 'Erkek')
country = ('Turkmenistan', 'Russia', 'London')
city = ('Ashgabat', 'Ahal', 'Balkan', 'Dashoguz', 'Mary', 'Lebap')

combo1 = ttk.Combobox(reg_frame, values=month, font=('Times', 16), foreground='darkred')
combo1.current()
combo1.grid(row=3, column=1, padx=6, pady=4)

combo2 = ttk.Combobox(reg_frame, values=numbers, font=('Times', 16), foreground='darkred')
combo2.current()
combo2.grid(row=4, column=1, padx=6, pady=4)

combo3 = ttk.Combobox(reg_frame, values=years, font=('Times', 16), foreground='darkred')
combo3.current()
combo3.grid(row=5, column=1, padx=6, pady=4)

combo4 = ttk.Combobox(reg_frame, values=gender, font=('Times', 16), foreground='darkred')
combo4.current()
combo4.grid(row=6, column=1, padx=6, pady=4)

combo5 = ttk.Combobox(reg_frame, values=country, font=('Times', 16), foreground='darkred')
combo5.current(0)
combo5.grid(row=7, column=1, padx=6, pady=4)

combo6 = ttk.Combobox(reg_frame, values=city, font=('Times', 16), foreground='darkred')
combo6.current(0)
combo6.grid(row=8, column=1, padx=6, pady=4)

btn_sub = Button(reg_frame, text='Submit', font=('Times', 18), fg='darkblue', command=subm,
                 height=1, width=8)
btn_sub.grid(row=11, column=0, padx=6, pady=4)
btn_clear = Button(reg_frame, text='Clear', font=('Times', 18), fg='darkblue', command=clear,
                   height=1, width=8)
btn_clear.grid(row=11, column=1, padx=6, pady=4)

y_scroll = Scrollbar(inf_frame, orient='vertical')
inf_text = Text (inf_frame, font=('Times', 14, 'bold'), yscrollcommand=y_scroll.set)
y_scroll.config(command=inf_text.yview)

y_scroll.pack(side=RIGHT, fill=Y)
inf_text.pack(fill=BOTH, expand=TRUE)

win.mainloop()