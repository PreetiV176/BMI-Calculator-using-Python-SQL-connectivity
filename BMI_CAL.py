from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as m

gui=Tk()
gui.title("BMI Calculator")
gui.geometry("470x580+300+200")
gui.resizable(False,False)
gui.configure(bg="#f0f1f5")

mydatabase=m.connect(host="localhost",user="root",password="Preeti@060599",database="bmi_cal")
cursor=mydatabase.cursor()


def BMI():
      
    try:
        h=float(height.get())
        w=float(weight.get())
        m=h/100                                                          # convert height into meter
        bmi=round(float(w/m**2),1)
        #print(bmi)
        Label_31.config(text=bmi,font="arial 40 bold",fg="dark green")
        
        
        if bmi<=18.5 :
            query_1="select Review from BMI where Ra between 0 and 18.5"
            cursor.execute(query_1)
            result_1=cursor.fetchall()
            Label_32.config(text=result_1)
            query_11="select Descrip from BMI where Ra between 0 and 18.5"
            cursor.execute(query_11)
            result_11=cursor.fetchall()
            Label_33.config(text=result_11)
        
        elif bmi>18.5 and bmi<=25 :
            query_2="select Review from BMI where Ra between 18.6 and 25"
            cursor.execute(query_2)
            result_2=cursor.fetchall()
            Label_32.config(text=result_2)
            query_21="select Descrip from BMI where Ra between 18.6 and 25"
            cursor.execute(query_21)
            result_21=cursor.fetchall()
            Label_33.config(text=result_21)
        
        elif bmi>25 and bmi<=30 :
            query_3="select Review from BMI where Ra between 26 and 30"
            cursor.execute(query_3)
            result_3=cursor.fetchall()
            Label_32.config(text=result_3)
            query_31="select Descrip from BMI where Ra between 26 and 30"
            cursor.execute(query_31)
            result_31=cursor.fetchall()
            Label_33.config(text=result_31)
        
        else :
            query_4="select Review from BMI where Ra between 31 and 100"
            cursor.execute(query_4)
            result_4=cursor.fetchall()
            Label_32.config(text=result_4)
            query_41="select Descrip from BMI where Ra between 31 and 100"
            cursor.execute(query_41)
            result_41=cursor.fetchall()
            Label_33.config(text=result_41)

        
    except Exception as e:
        Label_31.config(text=" Invalid \nDetails",font="arial 20 bold", fg="red")
    
        
    
#icon 
image=Image.open("icon.jpg")
re_image=image.resize((70,70))
tk_image=ImageTk.PhotoImage(re_image)
Label_1= Label(gui, image=tk_image)
Label_1.place(x=0,y=0)

#top
top=Image.open("top.jpg")
re_image_top=top.resize((200,50))
tk_image_top=ImageTk.PhotoImage(re_image_top)
Label_2=Label(gui, image=tk_image_top)
Label_2.place(x=150,y=10)

#bottom box
Label(gui,width=72,height=18,bg="light blue").pack(side=BOTTOM)

#two boxes
box_1=Image.open("box.jpg")
re_image_box=box_1.resize((200,200))
tk_box_1=ImageTk.PhotoImage(re_image_box)
tk_box_2=ImageTk.PhotoImage(re_image_box)
Label(gui,image=tk_box_1).place(x=30,y=100)
Label(gui,image=tk_box_2).place(x=250,y=100)


Label_height=Label(gui,text="HEIGHT [in cm]",font="arial 15 bold", bg="lightblue" , fg="#fff")
Label_height.place(x=60,y=110)
Label_Weight=Label(gui,text="WEIGHT [in kg]",font="arial 15 bold", bg="lightblue" , fg="#fff")
Label_Weight.place(x=280,y=110)


################ SLIDER 1 ###################

current_value= tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())
    
# command to change background color of scale
style = ttk.Style()
style.configure("TScale",background='light yellow')

slider=ttk.Scale(gui,from_=0 ,  to=400 ,  orient="horizontal" , style="TScale", command=slider_changed , variable=current_value)
slider.place(x=80 , y=250)

# #############################################

# #@@@@@@@@@@@@@@ SLIDER 2 @@@@@@@@@@@@@@@@@@@@

current_value2= tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())

# command to change background color of scale
style2 = ttk.Style()
style2.configure("TScale",background='light yellow')

slider2=ttk.Scale(gui,from_=0 ,  to=100 ,  orient="horizontal" , style="TScale", command=slider_changed2 , variable=current_value2)
slider2.place(x=300 , y=250)

# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Entry box
Height=StringVar()
Weight=StringVar()
height=Entry(gui,textvariable=Height,width=5,font="arial 50",bg="#fff",bd=0,justify=CENTER)  #to allign in center
height.place(x=35,y=160)
Height.set(get_current_value())

weight=Entry(gui,textvariable=Weight,width=5,font="arial 50",bg="#fff",bd=0,justify=CENTER)  #to allign in center
weight.place(x=255,y=160)
Weight.set(get_current_value2())

Button(gui, text="View Report", width=15 , height=2, font= "arial 10 bold", bg="#1f6e68", fg="white", command= BMI).place(x=320,y=320)

Label_31=Label(gui, bg="lightblue" , fg="#fff")
Label_31.place(x=30,y=315)

Label_32=Label(gui, font="arial 30 bold", bg="lightblue" , fg="#3b3a3a")
Label_32.place(x=30,y=400)

Label_33=Label(gui, font="arial 15 bold", bg="lightblue")
Label_33.place(x=30,y=470)

gui.mainloop()
