import os
import pickle
a = 0
list_yes = ["yes", "yep", "yeh", "yeah", "oui", "ouai", "ouais", "oi", "ya", "ja", "da"]
list_no = ["no", "nop", "nope", "niet", "nein", "nn", "non", "nen", "not", "nan", "na", "nah"]
list_type = ["verb", "noun", "adjective", "adverb", "preposition", "article", "determinant", "pronoun", "coordinating cunjonction", "subordonnating conjunction", "ponctuation", "other"]
error = ["Veuillez saisir un nom de langage valide", "Veuillez saisir un mot existant", "Veuillez saisir une commande existante", "Veuillez bien répondre", "Mot déjà existant"]
def search_language(var): #Search language
    n_glossary = quickload()
    try:
        var = int(var)
    except:
        pass
    if type(var) == int:
        for name, language in n_glossary.items():
            if var == language["id"]:
                n_name = name
                n_language = language
                id0 = language["id"]
                key0 = language["key"]
                n_list = [n_name, n_glossary, n_language, id0, key0]
                return n_list
    elif type(var) == str:
        for name, language in n_glossary.items():
            if var == language["key"] or var == name:
                n_name = name
                n_language = language
                id0 = language["id"]
                key0 = language["key"]
                n_list = [n_name, n_glossary, n_language, id0, key0]
                return n_list
            return n_list
    else:
        print(error[0])
        return 0
def print_language(word):
    pass
def search_word(var, words): #test the existence of a word
    try:
        var = int(var)
        for name, word in words.items():
            if word[0] == var:
                n_word = [name, word]
                return n_word #contient nom du mot et le mot
    except:
        for name, word in words.items():
            if word[1] == var or name == var:
                n_word = [name, word]
                return n_word #contient nom du mot et le mot
    else:
        print(error[1])
        return 0
def quickload():
    try:
        with open("mdl/data", "rb") as file:
            data = pickle.load(file)
            return data
    except:
        with open("data", "rb") as file:
            data = pickle.load(file)
            return data
def save_data(glossary):
    """glossary = {
    "ngunle": {
        "word": {
            "soman": [
                0, "soman01", [ #data
                    None, [
                        [
                            ["Etre humain"], ["L'être humain mange du pain"], 1, "soman11"
                        ]
                    ]
                ]
            ]
        },
        "id": 0,
        "key": "ngunle0_1"
    }
    }"""
    try:
        with open("mdl/data", "wb") as file:
            pickle.dump(glossary, file)
    except:
        with open("data", "wb") as file:
            pickle.dump(glossary, file)
def create_word(n_word, words, process): #n_word comprend les infos du mot et words l'ensemble des mots
    pass
def print_word(n_word):
    name = n_word[0]
    word = n_word[1]
    id_word = word[0]
    key_word = word[1]
    data_word = word[2]
    print(f"name {id_word}\n{key_word}")
    for ind, elt in enumerate(data_word):
        if elt != None:
            for indice, element in enumerate(list_type):
                if ind == indice:
                    print(f"    {element}")
                    for indice0, element0 in enumerate(elt):
                        trsl = element0[0]
                        ex = element0[1]
                        id1 = element0[2]
                        key1 = element0[3]
                        trsl1 = " ".join(trsl)
                        print(f"         {trsl1} id:{id1}")
                        for example in enumerate(ex):
                            print("         ex: ",example)
                        print(f"         key:{key1}")
def commands_word(var, words):
    if var == "help":
        pass
    elif type(var) != str() and len(var) < 3:
        print(error[2])
        return 0
    else:
        var = var.split(" ")
        if var[0] == "s":
            if var[1] == "word":
                try:
                    u_input = var[2]
                    n_word = search_word(u_input, words)
                    if n_word == 0:
                        print(error[2])
                        return 0
                    print_word(n_word)
                except:
                    print(error[2])
                    return 0
            if var[1] == "key":
                try:
                    #make a key generator and key searcher
                    pass
                except:
                    print(error[2])
                    return 0
            if var[1] == "id":
                try:
                    u_input = int(var[2])
                except:
                    print(error[2])
                    return 0
                n_word = search_word(u_input, words)
                if n_word == 0:
                    print(error[2])
                    return 0
                print_word(n_word)
            else:
                print(error[2])
                return 0
        elif var[0] == "e":
            if var[1] == "word":
                pass
            if var[1] == "key":
                pass
            if var[1] == "id":
                pass
            else:
                print(error[2])
                return 0
        elif var[0] == "d":
            if var[1] == "word":
                pass
            if var[1] == "key":
                pass
            if var[1] == "id":
                pass
            else:
                print(error[2])
                return 0
        elif var[0] == "c":
            glossary = quickload()
            var1 = search_word(var[2], words)
            if var1 != 0:
                    print(error[4])
                    return 0
            if var[1] == "word":
                u_choice = input("Translate: ")
                u_choice1 = input("Example: ")
                u_choice3 = input("Type: ")
                u_choice3 = u_choice3.lower()
                for elt in enumerate(list_type):
                    pass
                if elt != u_choice3:
                    print(error[4])
                    return 0
            elif var[1] == "trsl":
                u_choice = input("Translate: ")
                u_choice1 = input("Example: ")
                u_choice3 = input("Type: ")
                u_choice3 = u_choice3.lower()
                for elt in enumerate(list_type):
                    pass
                if elt != u_choice3:
                    print(error[4])
                    return 0
            u_choice2 = input(f"Are you sure to create: {var[2]}\ntype: {u_choice3}\ntrsl: {u_choice}\nex: {u_choice1}")
            if u_choice2.lower() == "oui":
                n_word = []
                create_word(n_word)
            else:
                print("Création annulée")
                return 0
        else:
            print(error[2])
            return 0
        print("5") 
def answer(answer0):
    answer0 = answer0.lower()
    for elt in list_no:
        if answer0 == elt:
            return "no"
    for elt in list_yes:
        if answer0 == elt:
            return "yes"
    else:
        print(error[3])
        return 0
#glossary = {"ngunle":{"word":{"soman":[0,"soman01",[None,[[[],[],1,"soman11"]]]]}}}
#save_data(glossary)
#search_language(a)
#input()
input()