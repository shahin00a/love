import turtle
import math
import time

# -------------------------------------------------
# LOVE HEART ANIMATION
# First screen: "Are you ready for this?"
# Click YES to start the heart animation.
# Click NO to close the program.
# -------------------------------------------------

screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.title("A Little Surprise")
screen.bgcolor("black")
screen.tracer(0)

# Text and button turtles
ui = turtle.Turtle()
ui.hideturtle()
ui.penup()
ui.speed(0)

button_drawer = turtle.Turtle()
button_drawer.hideturtle()
button_drawer.penup()
button_drawer.speed(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

OUTER_COLOR = "#ff5268"
INNER_COLOR = "#fff0c2"
LINE_COLOR = "#d8b968"

OUTER_WORDS = [
    "YOU ARE MY WORLD", "I LOVE YOU", "MY ONE AND ONLY",
    "FOREVER WITH YOU", "YOU MAKE ME HAPPY",
    "YOU ARE MY SUNSHINE", "ALWAYS IN MY HEART",
    "MY HEART IS YOURS", "YOU ARE SPECIAL",
    "LOVE YOU FOREVER", "YOU ARE MY HAPPINESS",
    "MY SWEETHEART", "YOU COMPLETE ME",
    "I CHOOSE YOU", "YOU ARE MY EVERYTHING"
]

INNER_WORDS = [
    "YOU ARE MY", "TRUE LOVE", "MY HAPPINESS",
    "MY FOREVER", "ALWAYS YOURS", "I LOVE YOU",
    "MY SWEET LOVE", "MY WORLD"
]


def draw_button(x, y, width, height, label, color):
    button_drawer.goto(x - width / 2, y - height / 2)
    button_drawer.pencolor(color)
    button_drawer.fillcolor(color)
    button_drawer.pensize(2)
    button_drawer.pendown()
    button_drawer.begin_fill()
    for _ in range(2):
        button_drawer.forward(width)
        button_drawer.left(90)
        button_drawer.forward(height)
        button_drawer.left(90)
    button_drawer.end_fill()
    button_drawer.penup()

    ui.goto(x, y - 10)
    ui.color("black")
    ui.write(label, align="center", font=("Arial", 16, "bold"))


def show_start_screen():
    ui.clear()
    button_drawer.clear()

    ui.goto(0, 145)
    ui.color("#fff0c2")
    ui.write("ARE YOU READY FOR THIS?",
             align="center", font=("Arial", 27, "bold"))

    ui.goto(0, 90)
    ui.color("#ff5268")
    ui.write("A little surprise is waiting for you...",
             align="center", font=("Arial", 16, "normal"))

    draw_button(-115, -5, 150, 55, "YES", "#d8b968")
    draw_button(115, -5, 150, 55, "NO", "#ff5268")

    ui.goto(0, -105)
    ui.color("#888888")
    ui.write("Choose YES or NO", align="center",
             font=("Arial", 11, "normal"))

    # Small creator credit at the very bottom.
    ui.goto(0, -375)
    ui.color("#777777")
    ui.write("made by shahin", align="center",
             font=("Arial", 9, "normal"))
    screen.update()


def heart_point(t, size):
    x = 16 * math.sin(t) ** 3
    y = (13 * math.cos(t) - 5 * math.cos(2 * t)
         - 2 * math.cos(3 * t) - math.cos(4 * t))
    return x * size, y * size


def draw_heart_outline(size, color, width=2):
    pen.penup()
    pen.pencolor(color)
    pen.pensize(width)

    for i in range(401):
        angle = 2 * math.pi * i / 400
        x, y = heart_point(angle, size)
        if i == 0:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)

    pen.penup()


def inside_heart(x, y, size):
    x = x / (16 * size)
    y = y / (16 * size)
    q = x * x + y * y - 1
    return q * q * q - x * x * y * y * y <= 0


def make_text_positions(size, step_x, step_y, exclude_size=None):
    positions = []
    y = -13.5 * size
    while y <= 14.5 * size:
        x = -16.5 * size
        while x <= 16.5 * size:
            if inside_heart(x, y, size):
                if exclude_size is None or not inside_heart(
                    x, y, exclude_size
                ):
                    positions.append((x, y))
            x += step_x
        y += step_y
    return positions


def write_word(x, y, word, color, font_size):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(word, align="center",
              font=("Georgia", font_size, "bold"))


def run_animation():
    # Remove the question and buttons before starting.
    ui.clear()
    button_drawer.clear()
    pen.clear()
    screen.bgcolor("black")
    screen.title("I LOVE YOU")
    screen.tracer(0)

    ui.goto(0, -375)
    ui.color("#777777")
    ui.write("made by shahin", align="center",
             font=("Arial", 9, "normal"))

    outer_size = 18
    inner_size = 8.7

    draw_heart_outline(outer_size, LINE_COLOR, 2)
    draw_heart_outline(inner_size, LINE_COLOR, 1)

    outer_positions = make_text_positions(
        outer_size, step_x=105, step_y=45,
        exclude_size=inner_size * 1.13
    )
    inner_positions = make_text_positions(
        inner_size, step_x=72, step_y=38
    )

    for index, (x, y) in enumerate(outer_positions):
        write_word(x, y, OUTER_WORDS[index % len(OUTER_WORDS)],
                   OUTER_COLOR, 10)
        screen.update()
        time.sleep(0.045)

    for index, (x, y) in enumerate(inner_positions):
        write_word(x, y, INNER_WORDS[index % len(INNER_WORDS)],
                   INNER_COLOR, 9)
        screen.update()
        time.sleep(0.055)

    pen.goto(0, -12)
    pen.color(INNER_COLOR)
    pen.write("I LOVE YOU", align="center",
              font=("Georgia", 22, "bold"))
    screen.update()


def handle_click(x, y):
    # YES button bounds
    if -190 <= x <= -40 and -32 <= y <= 22:
        screen.onclick(None)
        run_animation()

    # NO button bounds
    elif 40 <= x <= 190 and -32 <= y <= 22:
        ui.clear()
        button_drawer.clear()
        ui.goto(0, 0)
        ui.color("#fff0c2")
        ui.write("Maybe next time!", align="center",
                 font=("Arial", 22, "bold"))
        screen.update()
        time.sleep(1.2)
        screen.bye()


show_start_screen()
screen.onclick(handle_click)
screen.mainloop()
