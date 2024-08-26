import random
#import hangman art
from art import stages, logo
import hangman_words
from hangman_words import word_list

end_of_game = False

lives = 6

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

print(logo)

#testing code
# print(f"computer close [chosen_word]")

display = []

for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("guess a letter: ").lower()
    if guess in display:
        print(f"you have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "-" not in display:
        end_of_game = True
        print("you won!")
    if guess not in chosen_word:
        lives -= 1
        print(f"you have left with (lives) lives")
        if lives == 0:
            end_of_game = True
            print("you lose!")
            print(f"The chosen word was: {chosen_word}")
        print(stages[lives])
