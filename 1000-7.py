import os
import time
import pygame

os.system("cls")

print("Вы Гуль?")
choice = input("[1] Да [2] Нет = ")

if choice == "1":
    os.system("cls")
    count = 1000
    pygame.mixer.init()
    pygame.mixer.music.load("ghoul.mp3")
    pygame.mixer.music.play()
    time.sleep(1.618)
    print("Я ГУЛЬ....")
    time.sleep(2.611)
    os.system("cls")
    time.sleep(3.568)
    while count != -1:
        print(f"{count}-7={count-7}")
        count = count - 7
        time.sleep(0.07)
elif choice == "2":
    print("Пидора ответ.")
    os.system("pause")
