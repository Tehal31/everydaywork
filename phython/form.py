from tkinter import*
from mysql import connector
from tkinter import messagebox
def database():
    conn = connector.connect(
        user='root',
        password='Tehal',
        host='127.0.0.1',
        port='3306',
        database='tehaldb')
    mycursor = conn.cursor()
    mycursor.execute("insert into registrationform values(%s,%s,%s,%s,%s)",(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),var.get()))
    messagebox.showinfo("info","submitted")
    conn.commit()
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Sr_no",width=20,font=("bold", 10))
label_1.place(x=66,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="FullName",width=20,font=("bold", 10))
label_2.place(x=66,y=160)

entry_2 = Entry(root)
entry_2.place(x=240,y=160)

label_3 = Label(root, text="Roll_no",width=20,font=("bold", 10))
label_3.place(x=66,y=190)

entry_3 = Entry(root)
entry_3.place(x=240,y=190)

label_4 = Label(root, text="Address",width=20,font=("bold", 10))
label_4.place(x=66,y=220)

entry_4 = Entry(root)
entry_4.place(x=240,y=220)


label_5 =Label(root,text="Gender", width=20,font=("bold",10))
label_5.place(x=66,y=290)


var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=240,y=290)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=299,y=290)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database()).place(x=150,y=380)
root.configure(background = "grey")
root.mainloop()
print("registration form  seccussfully created...")