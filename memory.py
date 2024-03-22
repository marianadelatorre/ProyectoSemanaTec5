from random import *
from turtle import *

from freegames import path

car = path('car.gif')
emojis = ['\U0001F33C', '\U0001F337', '\U0001F31F', '\U0001F319', '\U0001F30A', '\U0001F48C', '\U0001F49F', '\U0001F493', '\U0001F48B', '\U0001F607', '\U0001F430', '\U0001F431', '\U0001F33E', '\U0001F490', '\U0001F9FA', '\U0001F6C1', '\U0001F43E', '\U0001FA70', '\U0001F375', '\U0001F9B7', '\U0001F340', '\U0001F331', '\U0001F344', '\U0001F324', '\U0001FA90', '\U0001F352', '\U0001F34B', '\U0001F37A', '\U0001F3D6', '\U0001F975', '\U0001F92D', '\U0001F925']
emojis *= 4 
shuffle(emojis)
state = {'mark': None}
hide = [True] * 64

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or emojis[mark] != emojis[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Ajustar la posición del texto para centrarlo en el cuadrado
        goto(x + 20, y + 10)
        color('black')
        write(emojis[mark], align="center", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
