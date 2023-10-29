import random
import json

# This line opens the json file.
jsonOpener= open("words.json")
# Loading the contents.
wordLibrary=json.load(jsonOpener)
# fetches a random word from the .json file.
chosenWord=random.choice(wordLibrary["words"])
# gets the lenght of the random chosen word.
wordLenght=len(chosenWord)
# displaying to the player how many letters are in the word.
display=[]+(["_"]*len(chosenWord))
# variable that stores the number of lives that the player has left(starts with 6).
life=6
# The fun and timeless animation of the original game that was played with pen and paper.
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# initilizez a list in wich the letters that have been a bad guess will be added
badGuesses=[]

while life>0:
    print(display)
    print("Bad guesses: "+str(badGuesses))
    print(stages[life])

    # If all underscores have been replaced with a letter, the word is complete and the player has won
    if "_" not in display:
        print("You Won")
        break 
    
    # Prompts the user to enter a letter
    guess = input("Guess a letter: ")
    
    # In case you want to end your game early(like i am doing while testing)
    if guess=="Finish" or guess=="finish":
        break

    #check if the user has entered a letter or a numeric value (let's hope he dosen't figure out we are not checking for boolean values)
    if guess.isalpha()==False:
        print("Invalid input!")
        print("Lives left: " + str(life))
        continue
        


    # In case the player  has entered more than one character
    if len(guess)>1:
        print("Please enter 1 letter at a time.")
        print("Lives left: " + str(life))
    
    # In case the player  has guessed a new letter
    elif guess in chosenWord:
            for position in range(wordLenght):
                letter=chosenWord[position]
                if letter==guess:
                    display[position]=guess
                else:
                    continue
    
    # In case of a bad guess
    elif guess not in chosenWord:
        life-=1
        print("Lives left :"+str(life))
        badGuesses.append(guess)
    
    # In case the player has already entered the letter
    elif guess in display:
        print("You already guessed that one")
        print("Lives left: " + str(life))
    elif not chosenWord.isalpha():
        print("Invalid input!")
        
# If too many bad guesses were made and variable life equals 0, the player loses            
if life==0:
    print("You Lost")
    print("The words was: "+str(chosenWord))
