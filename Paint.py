from turtle import *
from freegames import vector


def line(start, end):
    #Dibujar una línea de inicio a fin
    up() #levantar la pluma
    goto(start.x, start.y) #moverse a algun lugar
    down() #regresar la pluma
    goto(end.x, end.y)


def square(start, end):
    #Dibujar un cuadrado de inicio a fin
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4): #loop
        forward(end.x - start.x) #ubicacion
        left(90) #rota hacia la izquierda 4 veces

    end_fill()


def circle(start, end):
    #Dibujar un círculo de inicio a fin
    up() #levantar la pluma
    goto(start.x, start.y) #moverse a algun lugar
    down() #regresar la pluma

    import turtle
    turtle.circle((end.x - start.x)/2)

    end_fill()


def rectangle(start, end):
    #Dibujar un rectángulo de inicio a fin
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)
    end_fill()


def triangle(start, end):
    #Dibujar un triángulo de inicio a fin
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for i in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y): #Funcion de clicks
    #Guardar punto de inicio o dibujar figura.
    start = state['start'] #primer  click none

    if start is None:
        state['start'] = vector(x, y) #condicion guardar segunda entrada
    else: #Se realiza al tener una ubicacion guardada
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    #Guardar valor en state en key
    state[key] = value


state = {'start': None, 'shape': line} #condicion guaradar entrada
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u') #rehacer una accion
onkey(lambda: color('black'), 'K') #cam
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y') #color añadido
#teclas para elegir qué forma se va a hacer
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
