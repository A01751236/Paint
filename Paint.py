from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up() #levantar la pluma
    goto(start.x, start.y) #moverse a algun lugar 
    down() #regresar la pluma 
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4): #loop
        forward(end.x - start.x) #ubicacion
        left(90) #rota hacia la izquierda 4 veces

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up() #levantar la pluma
    goto(start.x, start.y) #moverse a algun lugar 
    down() #regresar la pluma 
    
    import turtle
    turtle.circle((end.x - start.x)/2)
    
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
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
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for i in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y): #Funcion de clicks
    "Store starting point or draw shape."
    start = state['start'] #primer  click none

    if start is None:
        state['start'] = vector(x, y) #condicion guardar segunda entrada
    else: #Se realiza al tener una ubicacion guardada 
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
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
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
