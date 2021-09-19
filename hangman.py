import random

# Write your code here
print("H A N G M A N")


words = ['python', 'java', 'kotlin', 'javascript']


guess = input("Guess the word: ")



if guess not in words:
    print("You lost!")
else:
    print("You survived!")