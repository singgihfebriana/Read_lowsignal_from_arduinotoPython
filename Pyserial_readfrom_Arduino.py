#Codeby Singgih Febriana

from time import sleep
import serial
from tkinter import*

root=Tk()
root.geometry("300x300")
label=Label(root,text="0",font=("arial",40))
label.pack()
ser=serial.Serial('/dev/ttyACM0',9600)
data=[]
while (True):
    value=ser.readline()
    encod=value.decode()
    x=encod.rstrip()
    label["text"]=[x]
    root.update()
    sleep(1)

root.mainloop()
