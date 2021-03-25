# Import modules to use
from words import palabras
import string
import random

# 1. Welcome
print("Welcome to the game hangman in Python")

# 2. Function to get word
def get_valid_word(palabras):
  word = random.choice(palabras)

  # Choose a good word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word.upper()

def hangman():

  word = get_valid_word(palabras) # SOL
  word_letters = set(word) # S, O , L
  alphabet = set(string.ascii_uppercase) # A, B, C, D, E,...
  used_letters = set()
  lives = 6
  print(type(word))
  print("La palabra es: ",word_letters)

  while len(word_letters) > 0:
    user_letter = input('Guess a letter:').upper() # S

    if user_letter in alphabet - used_letters: # si "S" esta en "A,B,C,D" - ""
      used_letters.add(user_letter) # S
      print(used_letters,'\n',word_letters)

      if user_letter in word_letters: # S es parte de tu palabra
        word_letters.remove(user_letter) # S, O , L le quito la S = O, L


      # else:
      #   lives = lives - 1
      #   print('Letter is not in word')

    elif user_letter in used_letters:
      print("You have already used that character. Please try again.")
    else:
      print("Invalid character. Please try again.")

    if len(word_letters) == 0:
      print("Your guessed the word: ", word)


hangman()


