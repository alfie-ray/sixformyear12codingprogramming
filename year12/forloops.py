import time
import os

# Simple Mario animation using ASCII art
frames = [
r"""
h
""",
r"""
he
""",
r"""
hell
""",
r"""
hello
""",
r"""
hell
""",
r"""
hel
""",
r"""
he
""",
r"""
h
""",
r"""

""",
]

for i in range(100):  # Repeat animation 8 times
    for frame in frames:
        os.system('cls')  # Clear screen (Windows)
        print(frame)
        time.sleep(0.001)