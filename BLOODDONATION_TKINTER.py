from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3

window=Tk()
window.geometry("600x500")
window.title("Blood Donation")
#*****************************************   MENU BAR   ***************************************

def exit1():
    messagebox.showinfo("exit","Thankyou for your donation !!")
    exit()

def abt():
    messagebox.showinfo("Welcome to about","This is a Blood donation registration page \n kindly fill your details to help others !! ")

def help1():
    messagebox.showinfo("Welcome to help","kindly refer w3shools ")
    
menu=Menu(window)
window.config(menu=menu)


subm1=Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Help",command=help1)

subm2=Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About",command=abt)

subm3=Menu(menu)
menu.add_cascade(label="Exit",command=exit1)

fn=StringVar()
ln=StringVar()
age1=StringVar()
var=StringVar()
r=StringVar()
var1=StringVar()
phone1=StringVar()
var5=StringVar()

#**************************************  DATABASE SQLITE 3   *********************************
def database():
    first11=fn.get()
    last11=ln.get()
    age11=age1.get()
    country11=var.get()
    gender11=r.get()
    blood11=var1.get()
    phone11=phone1.get()
    if first11 == '' or last11 == ''  or age11 == '' or country11 == '' or gender11 == '' or phone11 == '' or country11 == 'Select Country':
        messagebox.showwarning('Error','You need to Enter data in all the Fields')
    elif(age11.isalpha()):
        messagebox.showwarning('Error','Enter only digits')
    elif(int(age11)<17 or int(age11)>80):
        messagebox.showwarning('Error','Only Age limit >17 and <80 is allowed')
    elif(phone11.isalpha()):
        messagebox.showwarning('Error','Enter only digits')
    elif(len(phone11)!=10  or phone11[0]== "0" or phone11[0]== "1" or phone11[0]== "2" or phone11[0]== "3" or phone11[0]== "4" or phone11[0]== "5"):
        messagebox.showerror('Error','Enter 10 digit valid no')
    else:
        conn=sqlite3.connect("blooddonation.db")
        with conn:
            try:
                cursor=conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS chan (Name TEXT UNIQUE,Last TEXT,DOB TEXT,Country TEXT,Gender TEXT,BloodGroup TEXT,Phone Number TEXT)')
                cursor.execute('INSERT INTO chan(Name,Last,DOB,Country,Gender,BloodGroup,Phone) VALUES(?,?,?,?,?,?,?)',(first11,last11,age11,country11,gender11,blood11,phone11))
                messagebox.showinfo("Welcome","user is successfully registered!!!")
            except Exception as e:
                messagebox.showinfo("Error",e)


#**************************************   SEARCH USING BLOOD GROUP   *********************************

def search1():
    search1=Tk()
    search1.geometry("1100x500")
    search1.title("Search Blood")
    label01=Label(search1,text="Blood group",width=15,bg="skyblue", fg="white",font=("arial",15,"bold")).place(x=80,y=60)
    drop=ttk.Combobox(search1,value=["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    drop.current(0)
    drop.config(width=15)
    drop.place(x=330,y=67)
    '''var5=StringVar()
    var5.set("select Blood group")
    droplist5=OptionMenu(search11,var5,*list3)
    droplist5.config(width=15)
    droplist5.place(x=330,y=60)'''
    def search_now():
        var55=drop.get()
        print(var55)
        conn=sqlite3.connect("blooddonation.db")
        with conn:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM chan")
            rows1=cursor.fetchall()
            print(list(rows1))
            d2 = Label(search1, text="Name", font=("Courier New", 16, 'bold'))
            d2.place(x=75, y=100)
            d3 = Label(search1, text="Father Name", font=("Courier New", 16, 'bold'))
            d3.place(x=180, y=100)
            d4 = Label(search1, text="Age", font=("Courier New", 16, 'bold'))
            d4.place(x=380, y=100)
            d5 = Label(search1, text="Country", font=("Courier New", 16, 'bold'))
            d5.place(x=470, y=100)
            d6 = Label(search1, text="Gender", font=("Courier New", 16, 'bold'))
            d6.place(x=600, y=100)
            d7 = Label(search1, text="Blood Group", font=("Courier New", 16, 'bold'))
            d7.place(x=700, y=100)
            d8 = Label(search1, text="Phone Number", font=("Courier New", 16, 'bold'))
            d8.place(x=870, y=100)
            i=0
            x1=70
            y1=150
            x2=180
            x3=380
            x4=470
            x5=600
            x6=700
            x7=870

            flag=0
            for j in range(0,len(rows1)):
                if rows1[j][5] == var55:
                    flag=1
                    p1=Label(search1,text=rows1[j][0],font=("Courier New", 12, 'bold'))
                    p1.place(x=x1,y=y1)
                    p2=Label(search1,text=rows1[j][1],font=("Courier New", 12, 'bold'))
                    p2.place(x=x2,y=y1)
                    p3=Label(search1,text=rows1[j][2],font=("Courier New", 12, 'bold'))
                    p3.place(x=x3,y=y1)
                    p4=Label(search1,text=rows1[j][3],font=("Courier New", 12, 'bold'))
                    p4.place(x=x4,y=y1)
                    p4=Label(search1,text=rows1[j][4],font=("Courier New", 12, 'bold'))
                    p4.place(x=x5,y=y1)
                    p4=Label(search1,text=rows1[j][5],font=("Courier New", 12, 'bold'))
                    p4.place(x=x6,y=y1)
                    p4=Label(search1,text=rows1[j][6],font=("Courier New", 12, 'bold'))
                    p4.place(x=x7,y=y1)
                    y1 = y1 + 30
            if flag==0:
                messagebox.showwarning('Sorry','Sorry !! BloodGroup not available')

            b_quit=Button(search1,text="Quit",relief="solid",width=10,bg="red",fg="white",command=exit1).place(x=x4,y=y1+30)

            b_detail = Button(search1, text="All Details", relief="solid",width=10, bg="red", fg="white",command=detail1).place(x=x5,y=y1+30)

    b_login=Button(search1,text="search",width=15,bg="red",fg="white",command=search_now).place(x=630,y=60)
    search1.bind("<Return>")

#**************************************   DETAILS OF ALL THE USERS    *********************************

def detail1():
    con = sqlite3.connect('blooddonation.db')
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM chan")
        rows = cursor.fetchall()
        sho=Tk()
        sho.title("All Details")
        sho.geometry("1100x500")
        d1=Label(sho, text="All Details", font=("arial", 16, 'bold'), fg="red")
        d1.place(x=500,y=50)
        d2 = Label(sho, text="Name", font=("Courier New", 16, 'bold'))
        d2.place(x=75, y=100)
        d3 = Label(sho, text="Father Name", font=("Courier New", 16, 'bold'))
        d3.place(x=180, y=100)
        d4 = Label(sho, text="Age", font=("Courier New", 16, 'bold'))
        d4.place(x=380, y=100)
        d5 = Label(sho, text="Country", font=("Courier New", 16, 'bold'))
        d5.place(x=470, y=100)
        d6 = Label(sho, text="Gender", font=("Courier New", 16, 'bold'))
        d6.place(x=600, y=100)
        d7 = Label(sho, text="Blood Group", font=("Courier New", 16, 'bold'))
        d7.place(x=700, y=100)
        d8 = Label(sho, text="Phone Number", font=("Courier New", 16, 'bold'))
        d8.place(x=870, y=100)
        i=0
        x1=70
        y1=150
        x2=180
        x3=380
        x4=470
        x5=600
        x6=700
        x7=870
        for i in range(0,len(rows)):
            p1=Label(sho,text=rows[i][0],font=("Courier New", 12, 'bold'))
            p1.place(x=x1,y=y1)
            p2=Label(sho,text=rows[i][1],font=("Courier New", 12, 'bold'))
            p2.place(x=x2,y=y1)
            p3=Label(sho,text=rows[i][2],font=("Courier New", 12, 'bold'))
            p3.place(x=x3,y=y1)
            p4=Label(sho,text=rows[i][3],font=("Courier New", 12, 'bold'))
            p4.place(x=x4,y=y1)
            p4=Label(sho,text=rows[i][4],font=("Courier New", 12, 'bold'))
            p4.place(x=x5,y=y1)
            p4=Label(sho,text=rows[i][5],font=("Courier New", 12, 'bold'))
            p4.place(x=x6,y=y1)
            p4=Label(sho,text=rows[i][6],font=("Courier New", 12, 'bold'))
            p4.place(x=x7,y=y1)
            y1 = y1 + 30

            
        b_detail = Button(sho, text="Search", relief="solid",width=10, bg="red", fg="white",command=search1).place(x=x3,y=y1+30)

        b_quit=Button(sho,text="Quit",relief="solid",width=10,bg="red",fg="white",command=exit1).place(x=x4,y=y1+30)

        sho.bind("<Return>")

#**************************************  DECLARATION OF THE VARIABLE ,TEXTBOXES   *********************************
        
label1=Label(window,text="Blood donation Form",relief="solid",bg="orange",width=20,font=("arial",20,"bold")).place(x=120,y=5)

label2=Label(window,text="First Name",width=20,font=("arial",15,"bold")).place(x=70,y=60)
entry_2=Entry(window,textvar=fn).place(x=320,y=70)

label3=Label(window,text="Father Name",width=20,font=("arial",15,"bold")).place(x=80,y=100)
entry_3=Entry(window,textvar=ln).place(x=320,y=106)

label4=Label(window,text="Age",width=20,font=("arial",15,"bold")).place(x=38,y=140)
entry_4=Entry(window,textvar=age1).place(x=320,y=145)

label5=Label(window,text="Country",width=20,font=("arial",15,"bold")).place(x=57,y=180)
list1=["Nepal","India","China","Malaysia","America","Australia","Newzland","Bangladesh"]
droplist=OptionMenu(window,var,*list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=320,y=185)

label6=Label(window,text="Gender",width=20,font=("arial",15,"bold")).place(x=52,y=220)
r1=Radiobutton(window,text="Male",variable=r,value="Male").place(x=320,y=230)
r2=Radiobutton(window,text="Female",variable=r,value="Female").place(x=380,y=230)
r.set(False)


label7=Label(window,text="Blood group",width=20,font=("arial",15,"bold")).place(x=78,y=260)
drop1=ttk.Combobox(window,textvar=var1,value=["A+","A-","B+","B-","AB+","AB-","O+","O-"])
drop1.current(0)
drop1.config(width=15)
drop1.place(x=320,y=265)


label8=Label(window,text="Phone No.",width=20,font=("arial",15,"bold")).place(x=68,y=300)
entry_5=Entry(window,textvar=phone1).place(x=320,y=310)

b_login=Button(window,text="Submit",relief="solid",width=10,bg="red",fg="white",command=database).place(x=150,y=360)
window.bind("<Return>",database)

b_quit=Button(window,text="Quit",relief="solid",width=10,bg="red",fg="white",command=exit1).place(x=250,y=360)

b_detail = Button(window, text="All Details", relief="solid",width=10, bg="red", fg="white",command=detail1).place(x=350,y=360)
window.bind("<Return>")

b_detail = Button(window, text="Search", relief="solid",width=10, bg="red", fg="white",command=search1).place(x=450,y=360)
window.bind("<Return>")

window.mainloop()
