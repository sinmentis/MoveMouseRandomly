import sys
import time
import random
import pyautogui
import keyboard


def move_mouse_periodically(interval):
    while True:
        # Generate random coordinates
        screen_width, screen_height = pyautogui.size()
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_height)

        pyautogui.moveTo(random_x, random_y)
        print(f"Moved to {random_x}, {random_y}, press 'q' to exit")

        start_time = time.time()
        while time.time() - start_time < interval:
            if keyboard.is_pressed(hotkey="q"):
                print("Key pressed! Exiting the program.")
                return


def main():
    # Set the interval for mouse movement in seconds
    move_interval = 2  # seconds

    # Adjust mouse movement speed on Windows
    if sys.platform.startswith('win'):
        pyautogui.FAILSAFE = False

    try:
        move_mouse_periodically(move_interval)
    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    finally:
        # Restore FAILSAFE state
        pyautogui.FAILSAFE = True


if __name__ == "__main__":
    main()
