#this is my first repo in GitHub
#This is not a perfect Hangman game, but it is alright I guess.
#Note : I did not add Hangman art to the game

import requests

url = "https://random-word-api.herokuapp.com/word"

response = requests.get(url=url)

print('HANGMAN!!')
chances = 7
print(f"You have {chances} chances left.")

word = response.json()[0]

x = list(word)

d_list = []

for i in range(len(x)):
    d_list.append('_')

for value in d_list:
    print(value, end=' ')

print()

while chances != 0:
    letter = input('enter a letter:')
    if letter in x:

        for i in range(len(x)):
            if x[i] == letter:
                d_list[i] = letter

                for value in d_list:
                    print(value, end=' ')
                print()

    else:
        chances -= 1
        print('wrong guess')
        print(f'you have {chances} chance left')
        if chances == 0:
            print('you lost')
            print(f"The answer is {word}")

    if '_' not in d_list:
        print('you win')
        chances = 0
