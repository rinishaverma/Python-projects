import random
import os
from hangman_logo import logo,stages
print(logo)
from hangman_word_list import word_list
chosen_word=random.choice(word_list)
emoji1="\U0001F923"
emoji2="\U0001f600"
display=[]
lives=6
word_length=len(chosen_word)
for letter in range(word_length):
    display+="_"

end_of_game=False
while not end_of_game:
   guess=input("Enter the letter you think is present in the word:").lower()
   os.system('cls')
   print(f'You guessed {guess}')
   if guess not in chosen_word:
    lives-=1
    print(f'Oopsiee you guessed wrong letter {guess} ....We take of your life {emoji1}')
    print(display)
    if lives==0:
        end_of_game=True
        os.system('cls')
        
        print(f"Awwww!! You lose....The word was {chosen_word}")

   for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
          display[position]=letter
          print(display)
   for letter in display:
    if letter==guess:
            print("You have already chosed this letter")  
      
   
   if "_" not in display:
    end_of_game=True
    print("you win")
    print(f"Yippiiee!! You win...The word was {chosen_word} {emoji2}")
   print(stages[lives])
