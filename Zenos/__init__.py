from .banners import BANNERS
from .colors import Colors
from random import choice

ABOUT = """Zenos - Template Based Vulnerability Scanner inspired by Nuclei
https://github.com/zenython/zenos
"""
COLORS = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]

print(
    choice(COLORS) 
    + choice(BANNERS.split('---split---'))
    + '\n' + ABOUT
    + Colors.RESET)

