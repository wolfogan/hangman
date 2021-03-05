from words import palabras
import random

print("Welcome to the game hangman in Python")

def get_valid_word(palabras):
  word = random.choice(palabras)

  # Choose a goo word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word

my_word = get_valid_word(palabras)
print(my_word + '\n',len(my_word))

# silver
# * * * * * * *
# Una función que despliegue los guiones
# dependiendo el tamaño de la palabra


