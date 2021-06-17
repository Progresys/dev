import os
import pickle
from mdl.func import *
i = 0

while i == 0: #language
    user_choice = input("language: ")
    if user_choice == None:
        print(error[0])
        os.system("pause>nul")
        os.system("cls")
    else:
        now_list = search_language(user_choice)
        if now_list == 0:
            pass
        else:
            i = 1
while i == 1:
    words = now_list[2] #dict()
    words = words["word"]
    os.system("pause>nul")
    os.system("cls")
    user_choice = input(f"{now_list[0]}: ")
    if user_choice == "exit":
        u_choice = input("êtes vous sûr de quitter la partie: ")
        a = answer(u_choice)
        if a == "yes":
            i = 0
    elif len(user_choice) != 0:
        commands_word(user_choice, words)
    """ Search words
    now_word = search_word(user_choice, words)
    if now_word != 0:
        pass"""
