from os import name

class Colors:
    BLACK =  "\u001b[30m"
    RED =  "\u001b[31m"
    GREEN =  "\u001b[32m"
    YELLOW =  "\u001b[33m"
    ORANGE = "\u001b[38;5;208m"
    ORNAGE_YELLOW = "\u001b[38;5;184m"
    BLUE =  "\u001b[34m"
    MAGENTA =  "\u001b[35m"
    CYAN =  "\u001b[36m"
    WHITE =  "\u001b[37m"
    RESET =  "\u001b[0m"

    if name == 'nt':
        BLACK=RED=GREEN=YELLOW=ORANGE=ORNAGE_YELLOW\
            =BLUE=MAGENTA=CYAN=WHITE=RESET=''
