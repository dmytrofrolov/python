# "Stopwatch: The Game"
# You can try it here http://www.codeskulptor.org/#user30_D1KSMVX5Xg_14.py

import simplegui

# define global variables

current_time = 0
successful_stops = 0
total_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t1 = t // 10
    t2 = t1 // 60
    t3 = t1 % 60
    t4 = t3 // 10
    t5 = t3 % 10
    t6 = t % 10
    return str(t2) + ":" + str(t4) + str(t5) + "." + str(t6)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_time():
    timer.start()

def stop_time():
    global successful_stops, total_stops
    if timer.is_running() and format(current_time)[5:] == str(0):
        successful_stops += 1
    if timer.is_running():
        total_stops += 1
    timer.stop()
    
def reset_time():
    global current_time, successful_stops, total_stops
    timer.stop()
    current_time = 0
    successful_stops = 0
    total_stops = 0
   
def counter():
    return str(successful_stops) + " / " + str(total_stops)
    
# define event handler for timer with 0.1 sec interval
def timer():
    global current_time
    current_time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(current_time), [120, 150], 24, "White")
    canvas.draw_text(counter(), [230, 30], 24, "White")
    
# create frame
f = simplegui.create_frame("Stop the Watch!",300,300)

# register event handlers
f.add_button("Start", start_time, 100)
f.add_button("Stop", stop_time, 100)
f.add_button("Reset", reset_time, 100)
f.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer)

# start frame
f.start()

# Please remember to review the grading rubric

