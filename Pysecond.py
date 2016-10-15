# coding: utf-8
import turtle
import random
import math

def gotoXY(x,y):   # Функция переноса курсора
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def Circle(r,color):      # Функция заливки круга цветом
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def Draw_drum(x,y):      # Функция вырисовки обойм барабана с мушкой
    gotoXY(x, y)
    turtle.circle(80)
    gotoXY(x, y+160)
    Circle(5, 'red')
    for i in range(0, 7):
        phi_rad = (360/7) * i * math.pi / 180.0
        gotoXY(math.sin(phi_rad)*50 + x, math.cos(phi_rad)*50 + (y+60))
        Circle(22, 'white')

def Turn_drum(x,y):      # Функция анимации вращения барабана, возвращает значение остановки барабана
    for i in range(start, random.randrange(7, 100)):
        phi_rad = (360 / 7) * i * math.pi / 180.0
        gotoXY(math.sin(phi_rad) * 50 + x, math.cos(phi_rad) * 50 + (y + 60))
        Circle(22, 'brown')
        Circle(22, 'white')
    gotoXY(math.sin(phi_rad) * 50 + x, math.cos(phi_rad) * 50 + (y + 60))
    Circle(22, 'brown')
    return i

turtle.speed(0)

Draw_drum(100,100)

answer = ""
start = 0
while answer!= "n":
    answer = turtle.textinput("Крутим барабан?","y/n")
    if answer == "y":
        i = Turn_drum(100,100)
        start = i % 7
        if start == 0:   # Если пуля выстрелила
            gotoXY(-250, 250)
            turtle.write('Вы проиграли!', font = ("Arial", 18, "bold"))
    else:
        pass