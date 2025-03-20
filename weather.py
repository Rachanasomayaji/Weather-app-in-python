from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWeather():

    city=textfield.get()

    geolocator= Nominatim(user_agent="geoapiExrcises")
    location=geolocator.geocoder(city)
    obj =TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_ime=local_time.strftime("%I:%M %p")


#Search Box
Search_image=PhotoImage(file="download (1).png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="yellow")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="download (3).png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=600,y=30)

#logo
Logo_image=PhotoImage(file="download (4).png")
Logo=Label(image=Logo_image)
Logo.place(x=350,y=150)

Frame_image=PhotoImage(file="images.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)
clock.config(text=current_time)
name.config(text="CURRENT Weather")

#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="red",bg="#1ab5ef")
label1.place(x=280,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="red",bg="#1ab5ef")
label2.place(x=390,y=400)


label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="red",bg="#1ab5ef")
label3.place(x=520,y=400)


label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="red",bg="#1ab5ef")
label4.place(x=680,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=280,y=430)

h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=390,y=430)

d=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=520,y=430)

p=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()
