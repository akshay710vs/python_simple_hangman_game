import os
import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

#CHOOSE A WORD RANDOMLY FROM WORD LIST
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#A FLAG TO BREAK THE LOOP ONCE THE PLAYER WINS OR LOSES
end_of_game = False
lives = 6



#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#A BLANK LIST TO STORE THE DASHES AND CORRECT GUESSED LETTERS
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(logo)
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    #IF THE PLAYER USES ALREADY GUESSED LETTER
    if guess in display:
      print(f'You have already guessed letter {guess}')

    #CHECK GUESSED LETTER AND IF IT MATCHES WITH LETTER IN CHOSEN WORD, INSERT TO THE LETTER TO THE EXACT POSITION OF CHOSEN WORD IN DISPLAY LIST
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #CHECK IF THE PLAYER GUSSED WRONG LETTER
    if guess not in chosen_word:
        #A WARNING TO THE PLAYER AND LOSE A LIFE
        print(f"Guessed letter {guess} not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The Word is {chosen_word}")

    #ONCE THE PLAYER GUSSED ALL LETTER CORRECTLY. THE LETTERS IN THE DISPLAY LIST JOINS AND DISPLAYS THE WORD
    print(f"{' '.join(display)}")

    #CHECK IF PLAYER GOT ALL LETTERS
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #HANGMAN LIFE STAGES
    print(stages[lives])
    