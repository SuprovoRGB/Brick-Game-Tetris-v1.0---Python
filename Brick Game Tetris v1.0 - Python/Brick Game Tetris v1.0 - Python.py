#====================================================================================================
#====================================================================================================
# Program : Python - Brick Game Tetris v1.0
# By      : Suprovo Basak
# Date    : 15-August-2019
#====================================================================================================
#====================================================================================================

import os
import pygame
import random
import pysine
import array
import threading
import time

#====================================================================================================

pygame.init()
display_info = pygame.display.Info()
screen_resolution = (display_info.current_w, display_info.current_h)
window_resolution = (340,340)
window_position = (int(screen_resolution[0] / 2 - window_resolution[0] / 2), int(screen_resolution[1] / 2 - window_resolution[1] / 2))
os.environ["SDL_VIDEO_WINDOW_POS"] = "%i, %i" % (window_position)
window = pygame.display.set_mode(window_resolution)
pygame.display.set_caption("Python - Brick Game Tetris v1.0")
try:
    icon = pygame.image.load("Icon.png") # Resolution 32x32
    pygame.display.set_icon(icon)
except:
    pass

#====================================================================================================

B0 = 31
C1 = 33
CS1 = 35
D1 = 37
DS1 = 39
E1 = 41
F1 = 44
FS1 = 46
G1 = 49
GS1 = 52
A1 = 55
AS1 = 58
B1 = 62
C2 = 65
CS2 = 69
D2 = 73
DS2 = 78
E2 = 82
F2 = 87
FS2 = 93
G2 = 98
GS2 = 104
A2 = 110
AS2 = 117
B2 = 123
C3 = 131
CS3 = 139
D3 = 147
DS3 = 156
E3 = 165
F3 = 175
FS3 = 185
G3 = 196
GS3 = 208
A3 = 220
AS3 = 233
B3 = 247
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
CS5 = 554
D5 = 587
DS5 = 622
E5 = 659
F5 = 698
FS5 = 740
G5 = 784
GS5 = 831
A5 = 880
AS5 = 932
B5 = 988
C6 = 1047
CS6 = 1109
D6 = 1175
DS6 = 1245
E6 = 1319
F6 = 1397
FS6 = 1480
G6 = 1568
GS6 = 1661
A6 = 1760
AS6 = 1865
B6 = 1976
C7 = 2093
CS7 = 2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951
C8 = 4186
CS8 = 4435
D8 = 4699
DS8 = 4978

#--------------------------------------------------

notation_beethoven_ode_to_joy = [

[E4, 4], [E4, 4], [F4, 4], [G4, 4], [G4, 4], [F4, 4], [E4, 4], [D4, 4],
[C4, 4], [C4, 4], [D4, 4], [E4, 4], [E4, 6], [D4, 2], [D4, 8],
[E4, 4], [E4, 4], [F4, 4], [G4, 4], [G4, 4], [F4, 4], [E4, 4], [D4, 4],
[C4, 4], [C4, 4], [D4, 4], [E4, 4], [D4, 6], [C4, 2], [C4, 8],
[D4, 4], [D4, 4], [E4, 4], [C4, 4], [D4, 4], [E4, 2], [F4, 2], [E4, 4], [C4, 4],
[D4, 4], [E4, 2], [F4, 2], [E4, 4], [D4, 4], [C4, 4], [D4, 4], [G3, 8],
[E4, 4], [E4, 4], [F4, 4], [G4, 4], [G4, 4], [F4, 4], [E4, 4], [D4, 4],
[C4, 4], [C4, 4], [D4, 4], [E4, 4], [D4, 6], [C4, 2], [C4, 8]
]


notation_selection_sound = [

[G4, 2], [C5, 2], [D5, 2], [G5, 4],
[G4, 2], [C5, 2], [D5, 2], [G5, 4]
]


notation_ten_little_indian_boys = [

[C4, 8], [C4, 4], [C4, 4], [C4, 8], [C4, 4], [C4, 4], [E4, 8], [G4, 4], [G4, 4], [E4, 4], [D4, 4], [C4, 8],
[D4, 8], [D4, 4], [D4, 4], [D4, 8], [D4, 4], [D4, 4], [B3, 8], [D4, 4], [D4, 4], [B3, 4], [A3, 4], [G3, 8],
[C4, 4], [C4, 4], [C4, 4], [C4, 4], [C4, 8], [C4, 4], [C4, 4], [E4, 8], [G4, 4], [G4, 4], [E4, 4], [D4, 4], [C4, 8],
[D4, 8], [E4, 4], [F4, 4], [E4, 4], [C4, 4], [D4, 8], [C4, 24]
]


notation_score_sound = [

[C4, 2], [D4, 2], [E4, 2], [F4, 2], [G4, 2], [A4, 2], [B4, 2], [C5, 2], [D5, 2], [E5, 2]
]


notation_bizet_carmen = [

[C5, 8], [D5, 6], [C5, 2], [A4, 8], [A4, 8], [A4, 6], [G4, 2], [A4, 6], [AS4, 2], [A4, 16],
[AS4, 8], [G4, 6], [C5, 2], [A4, 16], [F4, 8], [D4, 6], [G4, 2], [C4, 16],
[G4, 16], [D5, 4], [C5, 4], [AS4, 4], [A4, 4], [G4, 4], [A4, 4], [AS4, 4], [A4, 16],
[E4, 8], [A4, 8], [A4, 8], [GS4, 6], [B4, 2], [E5, 32]
]

#==================================================

background_color = (230, 230, 230)
border_color = (205, 205, 205)

white = (255, 255, 255)
violet = (102, 45, 145)
indigo = (0, 0, 255)
blue = ( 0, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (242, 101, 34)
red = ( 255, 0, 0)
grey = (127, 127, 127)
black = (0, 0, 0)


colors = [violet, indigo, blue, green, yellow, orange, red]

#==================================================

bricks = [0] * 200

#--------------------------------------------------

bricks_image = [

0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 1, 1, 0, 0, 0, 1, 1, 0, 0,
1, 0, 0, 1, 0, 1, 0, 0, 1, 0,
1, 0, 0, 1, 0, 1, 0, 0, 1, 0,
0, 1, 1, 1, 0, 0, 1, 1, 1, 0,
0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
1, 1, 1, 0, 0, 1, 1, 1, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 1, 1, 0,
0, 1, 0, 0, 1, 0, 1, 0, 0, 1,
0, 1, 0, 0, 1, 0, 1, 0, 0, 1,
0, 0, 1, 1, 1, 0, 0, 1, 1, 1,
0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
0, 1, 1, 1, 0, 0, 1, 1, 1, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
1, 0, 1, 1, 0, 1, 0, 1, 1, 0,
1, 0, 1, 0, 1, 1, 0, 0, 1, 0,
1, 0, 1, 0, 0, 1, 0, 1, 1, 1,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

#==================================================

shape_o = [[2, 2],
1, 1,
1, 1
]

shape_i = [[1, 4],
1,
1,
1,
1
]

shape_l = [[2, 3],
1, 0,
1, 0,
1, 1
]

shape_j = [[2, 3],
0, 1,
0, 1,
1, 1
]

shape_s = [[3, 2],
0, 1, 1,
1, 1, 0
]

shape_z = [[3, 2],
1, 1, 0,
0, 1, 1
]

shape_t = [[3, 2],
1, 1, 1,
0, 1, 0
]


shapes = [shape_o, shape_i, shape_l, shape_j, shape_s, shape_z, shape_t]

#--------------------------------------------------

shape_letter_a = [[5, 5],
0, 1, 1, 1, 1,
1, 0, 0, 0, 0,
1, 0, 0, 1, 1,
1, 0, 0, 0, 1,
0, 1, 1, 1, 1
]


shape_number_01 = [[7, 5],
1, 1, 1, 0, 0, 1, 0,
1, 0, 1, 0, 1, 1, 0,
1, 0, 1, 0, 0, 1, 0,
1, 0, 1, 0, 0, 1, 0,
1, 1, 1, 0, 1, 1, 1
]

#==================================================

program_running = True
input_enabled = False
not_selected = True
move_x = 0
move_y = 30
rotate = 0

#====================================================================================================

def notation_play(notation, tempo):
    for n in range(len(notation)):
        pysine.sine(notation[n][0], notation[n][1] * tempo * 0.001)
        pysine.sine(0, 0.01)

#==================================================

def color_generate(options = colors):
    color = random.choice(options)
    return color

#--------------------------------------------------

def color_generate_without(color):
    options = colors.copy()
    options.remove(color)
    color1 = color_generate(options)
    return color1

#--------------------------------------------------

def dark_color_generate(color):
    dark_color = [0, 0, 0]
    for l in range(3):
        if (color[l] != 0):
            dark_color[l] = color[l] - 80
            if (dark_color[l] < 0):
                dark_color[l] = 0
    dark_color = tuple(dark_color)
    return dark_color

#==================================================

def brick_read(x, y):
    number = x + y * 10
    return bricks[number]

#--------------------------------------------------

def brick_write(color, x, y):
    number = x + y * 10
    bricks[number] = color

#--------------------------------------------------

def shape_read(shape, x, y):
    count = 1
    value = 0
    if (-1 < x and x < shape[0][0] and -1 < y and y < shape[0][1]):
        count += x + y * shape[0][0]
        value = shape[count]
    return value

#--------------------------------------------------

def shape_write(shape, value, x, y):
    count = 1
    if (-1 < x and x < shape[0][0] and -1 < y and y < shape[0][1]):
        count += x + y * shape[0][0]
        shape[count] = value

#==================================================

def shape_flip_horizontal(shape):
    shape1 = [0] * (shape[0][0] * shape[0][1] + 1)
    shape1[0] = shape[0]
    x = 0
    for x1 in range(shape[0][0] - 1, -1, -1):
        for y1 in range(shape[0][1]):
            shape_write(shape1, shape_read(shape, x1, y1), x, y1)
        x += 1
    return shape1

#--------------------------------------------------

def shape_rotate_clockwise(shape):
    shape1 = [0] * (shape[0][0] * shape[0][1] + 1)
    shape1[0] = [shape[0][1], shape[0][0]]
    for y in range(shape1[0][1]):
        for x in range(shape1[0][0]):
            shape_write(shape1, shape_read(shape, y, shape1[0][0] - 1 - x), x, y)
    return shape1

#--------------------------------------------------

def shape_letter_flip_step(shape_letter, step):
    shape = [0] * 26
    shape[0] = [5, 5]
    if (step == 0 or step == 8):
        shape = shape_letter
    elif (step == 1 or step == 3 or step == 5 or step == 7):
        if (step == 3 or step == 5):
            shape_letter = shape_flip_horizontal(shape_letter)
        for y in range(5):
            if (shape_read(shape_letter, 0, y) == 1 or shape_read(shape_letter, 1, y) == 1):
                shape_write(shape, 1, 1, y)
        for y in range(5):
            shape_write(shape, shape_read(shape_letter, 2, y), 2, y)
        for y in range(5):
            if (shape_read(shape_letter, 3, y) == 1 or shape_read(shape_letter, 4, y) == 1):
                shape_write(shape, 1, 3, y)
    elif (step == 2 or step == 6):
        for y in range(5):
            shape_write(shape, 1, 2, y)
    elif (step == 4):
        shape = shape_flip_horizontal(shape_letter)
    return shape

#==================================================

def shape_generate():
    shape = random.choice(shapes)
    n = random.randint(1, 4)
    for n1 in range(n):
        shape = shape_rotate_clockwise(shape)
    return shape

#--------------------------------------------------

def shape_spawn_xy(shape):
    x = 4
    if (0 < shape[0][0] - 2):
        x -= 1
    y = 0 - shape[0][1]
    location = [x, y]
    return location

#==================================================

def shape_can_x_move(shape, step, x, y):
    possible = True
    if (step < 0):
        if (0 < x):
            for y1 in range(y, y + shape[0][1]):
                for x1 in range(x, x + shape[0][0]):
                    if (shape_read(shape, x1 - x, y1 - y) == 1):
                        if (brick_read(x1 - 1, y1) != 0):
                            possible = False
        else:
            possible = False
    elif (0 < step):
        if (x + shape[0][0] < 10):
            for y2 in range(y, y + shape[0][1]):
                for x2 in range(x, x + shape[0][0]):
                    if (shape_read(shape, x2 - x, y2 - y) == 1):
                        if (brick_read(x2 + 1, y2) != 0):
                            possible = False
        else:
            possible = False
    else:
        possible = False
    return possible

#--------------------------------------------------

def shape_can_y_move(shape, x, y):
    possible = True
    if (y + shape[0][1] < 20):
        for y1 in range(y, y + shape[0][1]):
            for x1 in range(x, x + shape[0][0]):
                if (shape_read(shape, x1 - x, y1 - y) == 1):
                    if (-1 < y1 + 1):
                        if (brick_read(x1, y1 + 1) != 0):
                            possible = False
    else:
        possible = False
    return possible

#--------------------------------------------------

def shape_can_rotate(shape, x, y):
    shape1 = shape_rotate_clockwise(shape)
    possible = True
    if (y + shape1[0][1] < 21):
        for y1 in range(y, y + shape1[0][1]):
            for x1 in range(x, x + shape1[0][0]):
                if (shape_read(shape1, x1 - x, y1 - y) == 1):
                    if (brick_read(x1, y1) != 0):
                        possible = False
    else:
        possible = False
    return possible

#==================================================

def shape_to_bricks(shape, color, x, y):
    count = 1
    for y1 in range(y, y + shape[0][1]):
        for x1 in range(x, x + shape[0][0]):
            if (shape[count] == 1):
                if (-1 < x1 and x1 < 10 and -1 < y1 and y1 < 20):
                    brick_write(color, x1, y1)
            count += 1

#--------------------------------------------------

def bricks_x_full_check(y):
    full = True
    for x in range(10):
        if(brick_read(x, y) == 0):
            full = False
    return full

#--------------------------------------------------

def bricks_shift(y):
    while (0 < y):
        for x in range(10):
            brick_write(brick_read(x, y - 1), x, y)
        y -= 1
    for x in range(10):
        brick_write(0, x, 0)

#==================================================

def bricks_area_render():
    window.fill(border_color, [18, 18, 155, 305])
    window.fill(white, [20, 20, 151, 301])

#--------------------------------------------------

def next_shape_area_render():
    window.fill(border_color, [218, 78, 74, 74])
    window.fill(white, [220, 80, 70, 70])

#--------------------------------------------------

def message_area_render():
    window.fill(background_color, [181, 195, 150, 100])

#--------------------------------------------------

def text_render(text, size, bold, color, x, y):
    font = pygame.font.SysFont("arial", size)
    font.set_bold(bold)
    font_render = font.render(text, True, color)
    window.blit(font_render,(x, y))

#--------------------------------------------------

def canvas_render():
    window.fill(background_color)
    bricks_area_render()
    text_render("Brick Game", 15, False, black, 217, 20)
    text_render("Next :", 15, False, black, 217, 55)
    next_shape_area_render()
    text_render("Score :", 15, False, black, 217, 170)
    text_render("By : Suprovo Basak.", 15, False, black, 191, 303)

#--------------------------------------------------

def brick_render(color, x, y):
    dark_color = dark_color_generate(color)
    if (-1 < x and x < 10 and -1 < y and y < 20):
        pygame.draw.rect(window, black, (x * 15 + 20, y * 15 + 20, 16, 16))
        pygame.draw.rect(window, color, (x * 15 + 21, y * 15 + 21, 14, 14))
        pygame.draw.line(window, white, [x * 15 + 22, y * 15 + 22], [x * 15 + 33, y * 15 + 22])
        pygame.draw.line(window, white, [x * 15 + 33, y * 15 + 23], [x * 15 + 33, y * 15 + 33])
        pygame.draw.line(window, dark_color, [x * 15 + 22, y * 15 + 23], [x * 15 + 22, y * 15 + 33])
        pygame.draw.line(window, dark_color, [x * 15 + 23, y * 15 + 33], [x * 15 + 32, y * 15 + 33])

#--------------------------------------------------

def bricks_render(color = None):
    for y in range(20):
        for x in range(10):
            if (brick_read(x, y) != 0):
                if (color == None):
                    brick_render(brick_read(x, y), x, y)
                else:
                    brick_render(color, x, y)

#--------------------------------------------------

def shape_render(shape, color, x, y):
    for y1 in range(shape[0][1]):
        for x1 in range(shape[0][0]):
            if (shape_read(shape, x1, y1) == 1):
                brick_render(color, x + x1, y + y1)

#--------------------------------------------------

def bricks_image_render(color):
    global bricks
    global bricks_image
    bricks = bricks_image
    bricks_area_render()
    bricks_render(color)

#--------------------------------------------------

def next_shape_render(shape, color):
    x = 237
    y = 95
    dark_color = dark_color_generate(color)
    for y1 in range(y, y + 9 * shape[0][1], 9):
        for x1 in range(x, x + 9 * shape[0][0], 9):
            if (shape_read(shape, int((x1 - x) / 9), int((y1 - y) / 9)) == 1):
                pygame.draw.rect(window, black, (x1, y1, 10, 10))
                pygame.draw.rect(window, color, (x1 + 1, y1 + 1, 8, 8))
                pygame.draw.line(window, white, [x1 + 1, y1 + 1], [x1 + 8, y1 + 1])
                pygame.draw.line(window, white, [x1 + 8, y1 + 2], [x1 + 8, y1 + 8])
                pygame.draw.line(window, dark_color, [x1 + 1, y1 + 2], [x1 + 1, y1 + 8])
                pygame.draw.line(window, dark_color, [x1 + 2, y1 + 8], [x1 + 7, y1 + 8])

#==================================================

def animation_loop_fill(color):
    x = 0
    y = 0
    for l in range (5):
        for x1 in range(x, 10 - x):
            x = x1
            brick_render(color, x, y)
            pygame.display.flip()
            time.sleep(0.015)
        for y1 in range(y + 1, 20 - y):
            y = y1
            brick_render(color, x, y)
            pygame.display.flip()
            time.sleep(0.015)
        for x2 in range(x - 1, 8 - x, -1):
            x = x2
            brick_render(color, x, y)
            pygame.display.flip()
            time.sleep(0.015)
        for y2 in range(y - 1, 19 - y, -1):
            y = y2
            brick_render(color, x, y)
            pygame.display.flip()
            time.sleep(0.015)
        x += 1

#--------------------------------------------------

def animation_loop_fill_clear(color_fill, color_image = grey, bricks_image_hide = True):
    x = 0
    y = 0
    count = 0
    target = 0
    for l1 in range(200):
        if (bricks_image_hide == True):
            bricks_area_render()
        else:
            bricks_image_render(color_image)
        for l2 in range (5):
            for x1 in range(x, 10 - x):
                x = x1
                if (target < count):
                    brick_render(color_fill, x, y)
                count += 1
            for y1 in range(y + 1, 20 - y):
                y = y1
                if (target < count):
                    brick_render(color_fill, x, y)
                count += 1
            for x2 in range(x - 1, 8 - x, -1):
                x = x2
                if (target < count):
                    brick_render(color_fill, x, y)
                count += 1
            for y2 in range(y - 1, 19 - y, -1):
                y = y2
                if (target < count):
                    brick_render(color_fill, x, y)
                count += 1
            x += 1
        pygame.display.flip()
        time.sleep(0.015)
        x = 0
        y = 0
        count = 0
        target +=1

#--------------------------------------------------

def animation_fill(color):
    for y in range(19, -1, -1):
        for x in range(10):
            brick_render(color, x, y)
        pygame.display.flip()
        time.sleep(0.075)

#--------------------------------------------------

def animation_fill_clear(color_fill, color_image = grey, bricks_image_hide = True):
    for y in range(21):
        if (bricks_image_hide == True):
            bricks_area_render()
        else:
            bricks_image_render(color_image)
        for y1 in range(y, 20):
            for x1 in range(10):
                brick_render(color_fill, x1, y1)
        pygame.display.flip()
        time.sleep(0.075)

#--------------------------------------------------

def animation_blink(color):
    for l in range(4):
        bricks_area_render()
        pygame.display.flip()
        time.sleep(0.35)
        bricks_image_render(color)
        pygame.display.flip()
        time.sleep(0.35)

#--------------------------------------------------

def animation_opening():
    global bricks
    color1 = color_generate()
    color2 = color_generate_without(color1)
    animation_loop_fill(color1)
    animation_loop_fill_clear(color1, color2, False)
    animation_blink(color2)
    animation_loop_fill(color1)
    animation_fill_clear(color1)
    bricks = [0] * 200

#--------------------------------------------------

def animation_game_start():
    color1 = color_generate()
    animation_fill(color1)
    animation_fill_clear(color1)

#--------------------------------------------------

def animation_game_over():
    global bricks
    color1 = color_generate()
    color2 = color_generate_without(color1)
    animation_fill(color1)
    next_shape_area_render()
    animation_fill_clear(color1, color2, False)
    animation_blink(color2)
    animation_loop_fill(color1)
    animation_loop_fill_clear(color1, color2, False)
    bricks = [0] * 200

#==================================================

def game_menu():
    global not_selected
    x = 6
    y = 8
    flip_step = 0
    game_clear = 0
    flip_count = 1
    flip_full_cycle = 2
    count = 1
    while (not_selected):
        bricks_area_render()
        shape_render(shape_letter_flip_step(shape_letter_a, flip_step), violet, 2, 0)
        shape_render(shape_number_01, violet, 1, 15)
        if (game_clear == 0):
            shape_render(shape_i, indigo, 0, 10)
            shape_render(shape_l, red, 1, 11)
            shape_render(shape_z, blue, 2, 12)
            shape_render(shape_j, yellow, 6, 11)
            shape_render(shape_o, orange, 8, 12)
            shape_render(shape_t, green, x, y)
        else:
            brick_render(indigo, 0, 12)
            brick_render(indigo, 0, 13)
            brick_render(red, 1, 13)
            brick_render(yellow, 7, 13)
        if (3 <= count):
            if (4 < x):
                x -= 1
            elif (y < 12):
                y += 1
            else:
                if (game_clear < 3):
                    game_clear += 1
                else:
                    game_clear = 0
                    x = 6
                    y = 8
        if (flip_step < 8):
            flip_step += 1
        else:
            if (flip_count < flip_full_cycle):
                flip_step = 1
                flip_count += 1
            elif (flip_count < 15):
                flip_step = 8
                flip_count += 1
            else:
                flip_step = 1
                flip_count = 1
        if (3 <= count):
            count = 0
        count += 1
        pygame.display.flip()
        time.sleep(0.1)

#====================================================================================================

def main_process():
    global program_running
    global input_enabled
    global not_selected
    global move_x
    global move_y
    global rotate

    color1 = color_generate()
    color2 = color_generate_without(color1)
    shape1 = shape_generate()
    shape2 = shape_generate()
    shape_x, shape_y = shape_spawn_xy(shape1)
    shape_x_temporary, shape_y_temporary = shape_x, shape_y

    game_playing = True
    count_main = 1
    count_y = 1
    score = 0

    print("\n\nBRICK GAME TETRIS v1.0")
    print("\nControls :")
    print("\nMove   > 'Down', 'Left', 'Right'")
    print("Rotate > 'Space'")
    print("\n\nBy : Suprovo Basak.")


    clock = pygame.time.Clock()


    thread_sound = threading.Thread(target = notation_play, args = (notation_beethoven_ode_to_joy, 55,))
    thread_sound.daemon = True
    thread_sound.start()

    canvas_render()
    text_render("0", 15, False, black, 270, 170)
    animation_opening()

    input_enabled = True

    text_render("Press 'Enter'", 15, False, black, 214, 230)
    game_menu()
    message_area_render()

    thread_sound = threading.Thread(target = notation_play, args = (notation_selection_sound, 25,))
    thread_sound.daemon = True
    thread_sound.start()

    animation_game_start()

    thread_sound = threading.Thread(target = notation_play, args = (notation_ten_little_indian_boys, 33,))
    thread_sound.daemon = True
    thread_sound.start()
    thread_sound = threading.Thread(target = notation_play, args = (notation_bizet_carmen, 50,))
    thread_sound.daemon = True


    while (game_playing):
        if (3 <= count_main):
            for y in range(19, -1, -1):
                if (bricks_x_full_check(y) == True):
                    bricks_shift(y)
                    notation_play(notation_score_sound, 20)
                    score += 1

            if (rotate != 0):
                if (shape1[0][1] < shape1[0][0]):
                    shape_x_temporary = shape_x + 1
                    shape_y_temporary = shape_y - 1
                elif (shape1[0][0] < shape1[0][1]):
                    shape_x_temporary = shape_x - 1
                    shape_y_temporary = shape_y + 1
                else:
                    shape_x_temporary = shape_x
                    shape_y_temporary = shape_y
                if (shape_can_rotate(shape1, shape_x_temporary, shape_y_temporary) == True):
                    shape_x = shape_x_temporary
                    shape_y = shape_y_temporary
                    shape1 = shape_rotate_clockwise(shape1)
                    if (shape_x < 0):
                        shape_x = 0
                    elif (10 < shape_x + shape1[0][0]):
                        shape_x -= shape_x + shape1[0][0] - 10
                rotate = 0

            if (shape_can_x_move(shape1, move_x, shape_x, shape_y) == True):
                shape_x = shape_x + move_x
            move_x = 0

        if (move_y <= count_y):
            if (shape_can_y_move(shape1, shape_x, shape_y) == True):
                shape_y += 1
            elif (shape_y < 0):
                game_playing = False
                thread_sound.start()
            else:
                shape_to_bricks(shape1, color1, shape_x, shape_y)
                shape1 = shape2
                color1 = color2
                shape2 = shape_generate()
                color2 = color_generate_without(color1)
                shape_x, shape_y = shape_spawn_xy(shape1)


        if (3 <= count_main):
            canvas_render()
            bricks_render()
            shape_render(shape1, color1, shape_x, shape_y)
            next_shape_render(shape2, color2)
            text_render(str(score), 15, False, black, 270, 170)
            text_render("Controls :", 15, False, black, 210, 215)
            text_render("'Down', 'Left', 'Right'", 11, False, black, 210, 240)
            text_render("'Space'", 11, False, black, 210, 258)


        if (game_playing == False):
            message_area_render()
            text_render("Game Over", 20, False, black, 204, 228)
            animation_game_over()
            program_running = False


        if (3 <= count_main):
            count_main = 0
        count_main += 1

        if (move_y <= count_y):
            count_y = 0
        count_y += 1


        pygame.display.flip()
        clock.tick(30)

    thread_sound.join()

#====================================================================================================

def main():
    global program_running
    global input_enabled
    global not_selected
    global move_x
    global move_y
    global rotate


    main_clock = pygame.time.Clock()


    thread_main = threading.Thread(target = main_process,)
    thread_main.daemon = True

    thread_main.start()


    while (program_running):
        if (input_enabled == True):
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_LEFT]):
                move_x = -1
            if (keys[pygame.K_RIGHT]):
                move_x = 1


        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

            if (input_enabled == True):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_DOWN):
                        move_y = 3

                if (event.type == pygame.KEYUP):
                    if (event.key == pygame.K_RETURN):
                        not_selected = False
                    if (event.key == pygame.K_DOWN):
                        move_y = 30
                    if (event.key == pygame.K_SPACE):
                        rotate = 1


        main_clock.tick(30)


    thread_main.join()

#====================================================================================================

main()

#====================================================================================================
#====================================================================================================
# The End.
#====================================================================================================
#====================================================================================================
