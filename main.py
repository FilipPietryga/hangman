import csv
import random
import os

print("Welcome to the Hangman game!")
with open('words.txt') as file:
    reader = csv.reader(file, delimiter=',')
    words = []
    for row in reader:
        for item in row:
            words.append(item)
    print(words)
    word = random.choice(words)
    print(word)
    length = len(word)
    word_being_guessed = ""
    for i in range(length):
        word_being_guessed += "_"
    while True:
        os.system("cls")
        print(word_being_guessed)
        letter = input("Insert any letter: ")
        if letter in word:
            print("You have guessed the right letter!")
            index = 0
            temp = list(word_being_guessed)
            for l in word:
                if l == letter:
                    temp[index] = letter
                index += 1
            word_being_guessed = "".join(temp)
        if '_' not in word_being_guessed:
            print(word_being_guessed)
            print("You won!")
            exit()
