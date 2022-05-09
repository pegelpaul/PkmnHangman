from contextlib import nullcontext
import numbers
import random
import cgitb
from time import monotonic
from normal import normal
from ground import ground
from dragon import dragon
from ice import ice
from elektrik import elektrik
from fairy import fairy
from fire import fire
from flying import flying
from ghost import ghost
from rock import rock
from poison import poison
from bug import bug
from fighting import fighting
from grass import grass
from psychic import psychic
from steel import steel
from dark import dark
from water import water
from words import words

from hangman_visual import lives_visual_dict
import string

global streak
streak = 0
global type
type = 'null'

cgitb.enable()


def get_valid_word(words):
    global type
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    if (word in normal):
        type = 'Normal'
    elif (word in ground):
        type = 'Boden'
    elif (word in dragon):
        type = 'Drache'
    elif (word in ice):
        type = 'Eis'
    elif (word in elektrik):
        type = 'Elektro'
    elif (word in fairy):
        type = 'Fee'
    elif (word in fire):
        type = 'Feuer'
    elif (word in flying):
        type = 'Flug'
    elif (word in ghost):
        type = 'Geist'
    elif (word in rock):
        type = 'Gestein'
    elif (word in poison):
        type = 'Gift'
    elif (word in bug):
        type = 'Käfer'
    elif (word in fighting):
        type = 'Kampf'
    elif (word in grass):
        type = 'Pflanze'
    elif (word in psychic):
        type = 'Psycho'
    elif (word in steel):
        type = 'Stahl'
    elif (word in dark):
        type = 'Unlicht'
    elif (word in water):
        type = 'Wasser'

    return word.upper()


# def get_type():
    if (get_valid_word(words) in normal):
        type = 'Normal'
    elif (get_valid_word(words) in ground):
        type = 'Boden'
    elif (get_valid_word(words) in dragon):
        type = 'Drache'
    elif (get_valid_word(words) in ice):
        type = 'Eis'
    elif (get_valid_word(words) in elektrik):
        type = 'Elektro'
    elif (get_valid_word(words) in fairy):
        type = 'Fee'
    elif (get_valid_word(words) in fire):
        type = 'Feuer'
    elif (get_valid_word(words) in flying):
        type = 'Flug'
    elif (get_valid_word(words) in ghost):
        type = 'Geist'
    elif (get_valid_word(words) in rock):
        type = 'Gestein'
    elif (get_valid_word(words) in poison):
        type = 'Gift'
    elif (get_valid_word(words) in bug):
        type = 'Käfer'
    elif (get_valid_word(words) in fighting):
        type = 'Kampf'
    elif (get_valid_word(words) in grass):
        type = 'Pflanze'
    elif (get_valid_word(words) in psychic):
        type = 'Psycho'
    elif (get_valid_word(words) in steel):
        type = 'Stahl'
    elif (get_valid_word(words) in dark):
        type = 'Unlicht'
    elif (get_valid_word(words) in water):
        type = 'Wasser'
    return type.upper()


def try_again():
    param = input('try again? (y/n)').lower()

    if param == 'y':
        hangman()
    else:
        print('Thx for playing')


def hangman():
    word = get_valid_word(words)

    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    global streak
    global type
    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current Pokémon: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        elif user_letter == word:
            streak = streak+1
            print('YAY! You guessed the Pokémon', word,
                  '!!', 'Your streak increased to: ', streak)
            hangman()
        elif user_letter == 'HINT':
            print(type)
        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The Pokémon was',
              word, 'Your final streak is: ', streak)
        streak = 0
        try_again()
    else:
        streak = streak+1
        print('YAY! You guessed the Pokémon', word,
              '!!', 'Your streak increased to: ', streak)

        hangman()


if __name__ == '__main__':
    hangman()
