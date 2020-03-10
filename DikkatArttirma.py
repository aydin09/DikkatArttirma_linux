#!/usr/bin/python3
# BU PROGRAM GÖKSEL GÜRSU TARAFINDAN YAPILMIŞTIR.

from tkinter import *
import pygame
import time
import random

pygame.mixer.init()

pencere=Tk()
pencere.tk_setPalette("white")
pencere.attributes("-fullscreen", 1)
       
Label2=Label(text="1'den 20'ye kadar sayıları sırayla hızlı bir şekilde butonlara basarak tamamlayınız.",font="TTKBDikTemelAbece 12")
Label2.place(relx = 0.01, rely = 0.92)

Label4=Label(text="DİKKAT ARTTIRMA OYUNU",font="TTKBDikTemelAbece 20")
Label4.place(relx = 0.40, rely = 0.02)

label=Label(text="gokselgursu@gmail.com --- http://www.egitimhane.com/",font="TTKBDikTemelAbece 12")
label.place(relx = 0.74, rely = 0.95)

xy=[["0.08","0.1"],["0.16","0.1"],["0.24","0.1"],["0.32","0.1"],["0.4","0.1"],["0.48","0.1"],["0.56","0.1"],["0.64","0.1"],["0.72","0.1"],["0.8","0.1"],["0.88","0.1"], \
    ["0.08","0.2"],["0.16","0.2"],["0.24","0.2"],["0.32","0.2"],["0.4","0.2"],["0.48","0.2"],["0.56","0.2"],["0.64","0.2"],["0.72","0.2"],["0.8","0.2"],["0.88","0.2"], \
    ["0.08","0.3"],["0.16","0.3"],["0.24","0.3"],["0.32","0.3"],["0.4","0.3"],["0.48","0.3"],["0.56","0.3"],["0.64","0.3"],["0.72","0.3"],["0.8","0.3"],["0.88","0.3"], \
    ["0.08","0.4"],["0.16","0.4"],["0.24","0.4"],["0.32","0.4"],["0.4","0.4"],["0.48","0.4"],["0.56","0.4"],["0.64","0.4"],["0.72","0.4"],["0.8","0.4"],["0.88","0.4"], \
    ["0.08","0.5"],["0.16","0.5"],["0.24","0.5"],["0.32","0.5"],["0.4","0.5"],["0.48","0.5"],["0.56","0.5"],["0.64","0.5"],["0.72","0.5"],["0.8","0.5"],["0.88","0.5"], \
    ["0.08","0.6"],["0.16","0.6"],["0.24","0.6"],["0.32","0.6"],["0.4","0.6"],["0.48","0.6"],["0.56","0.6"],["0.64","0.6"],["0.72","0.6"],["0.8","0.6"],["0.88","0.6"], \
    ["0.08","0.7"],["0.16","0.7"],["0.24","0.7"],["0.32","0.7"],["0.4","0.7"],["0.48","0.7"],["0.56","0.7"],["0.64","0.7"],["0.72","0.7"],["0.8","0.7"],["0.88","0.7"], \
    ["0.08","0.8"],["0.16","0.8"],["0.24","0.8"],["0.32","0.8"],["0.4","0.8"],["0.48","0.8"],["0.56","0.8"],["0.64","0.8"],["0.72","0.8"],["0.8","0.8"],["0.88","0.8"]]
    
e=[]

q=0

while q<20:
    for d in random.sample((xy),1):
        e.append(d)
        xy.remove(d)
        q+=1

        break

h=e[0][0]
t=e[0][1]

h1=e[1][0]
t1=e[1][1]

h2=e[2][0]
t2=e[2][1]

h3=e[3][0]
t3=e[3][1]

h4=e[4][0]
t4=e[4][1]

h5=e[5][0]
t5=e[5][1]

h6=e[6][0]
t6=e[6][1]

h7=e[7][0]
t7=e[7][1]

h8=e[8][0]
t8=e[8][1]

h9=e[9][0]
t9=e[9][1]

h10=e[10][0]
t10=e[10][1]

h11=e[11][0]
t11=e[11][1]

h12=e[12][0]
t12=e[12][1]

h13=e[13][0]
t13=e[13][1]

h14=e[14][0]
t14=e[14][1]

h15=e[15][0]
t15=e[15][1]

h16=e[16][0]
t16=e[16][1]

h17=e[17][0]
t17=e[17][1]

h18=e[18][0]
t18=e[18][1]

h19=e[19][0]
t19=e[19][1]

def aşama20():
    import time
    global toplam1

    pygame.mixer.music.load("alkis.ogg")
    pygame.mixer.music.play()

    time.sleep(3)

    time22 = time.strftime("%H:%M:%S")
    time2 = time.strftime("%H %M %S")

    sonu1=Label(text="Oyunu Bitiriş Zamanı     "+time22,font="TTKBDikTemelAbece 16")
    sonu1.place(relx = 0.4, rely = 0.91)

    zaman2=time2.split()
    saat2=int(zaman2[0])*3600
    dakika2=int(zaman2[1])*60
    saniye2=int(zaman2[2])
    toplam2=saat2+dakika2+saniye2

    zamanfark=int(toplam2 - toplam1)
    saatler=zamanfark//3600
    dakikalar=zamanfark%3600//60
    saniyeler=zamanfark%60

    sonu2=Label(text="Geçen Süre                "+str(saatler)+":"+str(dakikalar)+":"+str(saniyeler),font="TTKBDikTemelAbece 16")
    sonu2.place(relx = 0.4, rely = 0.96)
        
    pygame.mixer.music.load("fon.ogg")
    pygame.mixer.music.play(-1)
    
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama19():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",command=aşama20,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama18():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",command=aşama19,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama17():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",command=aşama18,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama16():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",command=aşama17,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama15():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",command=aşama16,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama14():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",command=aşama15,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama13():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",command=aşama14,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama12():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",command=aşama13,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama11():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",command=aşama12,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama10():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",command=aşama11,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama9():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",command=aşama10,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama8():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",command=aşama9,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama7():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",command=aşama8,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama6():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",command=aşama7,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama5():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",command=aşama6,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama4():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",command=aşama5,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama3():
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",command=aşama4,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama2():    
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",command=aşama3,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama1():    
    birer = Button()
    birer.config(text="1",fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",command=aşama2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

birer = Button()
birer.config(text="1",command=aşama1,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer.place(relx = h , rely = t)

ikişer = Button()
ikişer.config(text="2",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer.place(relx = h1, rely = t1)

birer1 = Button()
birer1.config(text="3",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer1.place(relx = h2 , rely = t2)

ikişer1 = Button()
ikişer1.config(text="4",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer1.place(relx = h3, rely = t3)

birer2 = Button()
birer2.config(text="5",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer2.place(relx = h4 , rely = t4)

ikişer2 = Button()
ikişer2.config(text="6",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer2.place(relx = h5, rely = t5)

birer3 = Button()
birer3.config(text="7",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer3.place(relx = h6 , rely = t6)

ikişer3 = Button()
ikişer3.config(text="8",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer3.place(relx = h7, rely = t7)

birer4 = Button()
birer4.config(text="9",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer4.place(relx = h8 , rely = t8)

ikişer4 = Button()
ikişer4.config(text="10",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer4.place(relx = h9, rely = t9)

birer5 = Button()
birer5.config(text="11",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer5.place(relx = h10 , rely = t10)

ikişer5 = Button()
ikişer5.config(text="12",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer5.place(relx = h11, rely = t11)

birer6 = Button()
birer6.config(text="13",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer6.place(relx = h12 , rely = t12)

ikişer6 = Button()
ikişer6.config(text="14",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer6.place(relx = h13, rely = t13)

birer7 = Button()
birer7.config(text="15",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer7.place(relx = h14 , rely = t14)

ikişer7 = Button()
ikişer7.config(text="16",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer7.place(relx = h15, rely = t15)

birer8 = Button()
birer8.config(text="17",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer8.place(relx = h16 , rely = t16)

ikişer8 = Button()
ikişer8.config(text="18",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer8.place(relx = h17, rely = t17)

birer9 = Button()
birer9.config(text="19",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer9.place(relx = h18 , rely = t18)

ikişer9 = Button()
ikişer9.config(text="20",fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer9.place(relx = h19, rely = t19)

pygame.mixer.music.load("hello.ogg")
pygame.mixer.music.play(-1)

time11 = time.strftime("%H:%M:%S")
time1 = time.strftime("%H %M %S")

zaman1=time1.split()
saat1=int(zaman1[0])*3600
dakika1=int(zaman1[1])*60
saniye1=int(zaman1[2])
toplam1=saat1+dakika1+saniye1

sonu=Label(text="Oyuna Başlama Zamanı  "+time11,font="TTKBDikTemelAbece 16")
sonu.place(relx = 0.4, rely = 0.86)

buton=Button()
buton.config(text="ÇIKIŞ",command=pencere.destroy,width='10',fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
buton.place(relx = 0.89, rely = 0.86)
      
pencere.mainloop()
