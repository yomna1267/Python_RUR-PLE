def turn_right():
    repeat(turn_left,3)
def go():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
while not on_beeper():
    go()
else:
    pick_beeper()
turn_off()