from pyautogui import click
from time import sleep
from keyboard import is_pressed

if __name__ == '__main__':
    print("Press escape to stop the clicker")
    while True:
        y = int(input("Input the time between clicks (milisec)"))
        while True:
            click()
            if is_pressed('esc'):
                break
            sleep(y/1000)
        print("\nclicker finished\n")


