import time 
import sys

lyrics = [
    ("Mungkin aku bukan pemberani", 0.08),
    ("Mungkin aku lelah dengan sang ilahi", 0.13),
    ("Tapi kau masih disini", 0.08),
    ("Di jiwa yang t'lah mati", 0.08),
    ("Mungkin masih ada esok hari", 0.12)
]

delay = [5.8, 6.3, 3.7, 3.5]

def animate_text(text, char_delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    for i, (text, char_delay) in enumerate(lyrics):
        animate_text(text, char_delay)
        if i < len(lyrics) - 1:
            next_line_delay = max(0, delay[i % len(delay)] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()