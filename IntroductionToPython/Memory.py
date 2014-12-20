# implementation of card game - Memory
# you can try it here: http://www.codeskulptor.org/#user31_rn5tBViMN5kKw51.py

import simplegui
import random

# helper function to initialize globals
def new_game():
    global d, state, turns, numbers, cur_open
    cur_open = [-1, -1]
    d = {}
    state = 0
    turns = 0
    numbers = range(8)
    numbers.extend(numbers)
    random.shuffle(numbers)
    for n in range(16):
        d[n] = [False, False, numbers.pop()]
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, d, turns, cur_open
    if d[pos[0]/50][0] == False and d[pos[0]/50][1] == False:
        if state == 0:
            state = 1
            cur_open[0] = pos[0] / 50
            d[cur_open[0]][1] = True
        elif state == 1:
            state = 2
            cur_open[1] = pos[0] / 50
            d[cur_open[1]][1] = True
        else:
            state = 1
            if d[cur_open[0]][2] != d[cur_open[1]][2]:
                d[cur_open[0]][1] = False
                d[cur_open[1]][1] = False
            cur_open[0] = pos[0] / 50
            d[cur_open[0]][1] = True
            turns += 1    
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global d, turns
    label.set_text('Turns = '+str(turns))
    for n in range(16):
        if d[n][0] == True or d[n][1] == True:
           canvas.draw_polygon([(n*50, 0), (n*50+50, 0), (n*50+50, 100), (n*50,100)], 2, 'White' ,'Black')
           canvas.draw_text(str(d[n][2]), (n*50+10, 70), 55, 'White')
        else:
            canvas.draw_polygon([(n*50, 0), (n*50+50, 0), (n*50+50, 100), (n*50,100)], 2, 'Red', 'Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric