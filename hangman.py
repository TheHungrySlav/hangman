import random
from words import words
import string

def valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Letters Used
        print('You have',lives, 'lives remaining')
        print(word)
        print(word_letters)
        print('You have used these letters: ', ' '.join(used_letters))
        
        #Current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            elif user_letter not in word_letters:
                lives -= lives    
        elif user_letter in used_letters:
            print('You used this letter, please choose another')

        else:
            print('Invalid Character')


    print(word_list)
    print('You win! ')

hangman()