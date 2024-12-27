# Theme: `Dark visual studio` -> `One dark pro monokai darker`
# Installed `Python Extension Pack`

from time import sleep
import random


LINE_UP_CHAR = "\033[F"
CLEAR_LINE_CHAR = "\033[K"
GO_TO_START_CHAR = "\r"
TERMINAL_WIDTH = 100
STEP = 3


# List of different colors
COLOR_LIST = [
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]

GUN_COLOR = "\033[31m"      # Red color
RESET_COLOR = "\033[0m"     # Reset color
BULLET_COLOR = "\033[31m"   # Red color
CAR_COLOR = "\033[31m"      # Red color

def pick_random_color():
    return random.choice(COLOR_LIST)

gun = """   {bullet_color}
 {spc} :    {gun_color}
 {spc} ^  
 {spc}/*\  
 {spc}---   {reset_color}
"""

right_dir = True
curr_pos = 4


print("\n"*50)

try:
    while (True):
        if right_dir and curr_pos < TERMINAL_WIDTH - 5:
            curr_pos += STEP
        elif right_dir:
            right_dir = False
            BULLET_COLOR = pick_random_color()
            CAR_COLOR = pick_random_color()

        if not right_dir and curr_pos > 2:
            curr_pos -= STEP
        elif not right_dir:
            right_dir = True
            BULLET_COLOR = pick_random_color()
            CAR_COLOR = pick_random_color()
            
        sleep(0.08)        
        lines = gun.count("\n") - 1

        for i in range(lines - 1):
            print(LINE_UP_CHAR + CLEAR_LINE_CHAR, end='')

        print(LINE_UP_CHAR, end='')
        print(gun.format(
            spc= " " * curr_pos,
            bullet_color=BULLET_COLOR,
            gun_color=CAR_COLOR,
            reset_color=RESET_COLOR
            ), end='')


except KeyboardInterrupt:
    print(gun.format(spc=" " * curr_pos))
    print("\nExiting...")
    exit(0)        


