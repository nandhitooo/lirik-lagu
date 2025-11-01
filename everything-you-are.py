import time
import sys

lyrics = [
    ("Ceeeeeeeeriiiiiita kita tak jauh berbeda", 0.15),
    ("Got beat down by the world", 0.08),
    ("Sometimes I wanna fold", 0.08),
    ("Namun suratmu kan ku ceritakan ke anak-anakku nanti", 0.06),
    ("Bahwa aku pernah dicintai", 0.10),
    ("With everything u are", 0.09),
]

delay = [7, 3, 2.45, 4.7, 5.5]

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