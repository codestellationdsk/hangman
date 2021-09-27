import random
def hangman():

     words_list = ["elephant","rabbit","lion","tiger","zebra","giraffe","panther","donkey","monkey","deer","gorilla","chimpanzee"]
     word = random.choice(words_list)
     turns=10
     guessed= ''
     valid_entry = set('abcdefghijklmnopqrstuvwxyz')

     while len(word)>0:
         correctWord=""
    
         for letter in word: 
              if letter in guessed:
                 correctWord = correctWord + letter
              else:
                 correctWord = correctWord + "_"
              if correctWord == word:
                 print(correctWord)
                 print("Congratulations!!! ***You Won!***")
                 break            
    
         print ("The word is",correctWord)
         guess = input()
  
         if guess in valid_entry:
             guessed = guessed + guess
         else:
              print("Enter a valid character")
              guess = input()
         if guess not in word:
             turns = turns-1
    
             if turns == 9:
                print("You have 9 turns left")
                print("---------")
                print("      O  ")
             if turns == 8:
                print("You have 8 turns left")
                print("---------")
                print("      O  ")
                print("      |  ")
             if turns == 7:
                print("You have 7 turns left")
                print("---------")
                print("      O  ")
                print("      |  ")
                print("      |  ")
             if turns == 6:
                print("You have 6 turns left")
                print("---------")
                print("      O  ")
                print("      |/ ")
                print("      |  ")
             if turns == 5:
                print("You have 5 turns left")
                print("---------")
                print("      O  ")
                print("     \|/ ")
                print("      |  ")
             if turns == 4:
                print("You have 4 turns left")
                print("---------")
                print("      O  ")
                print("     \|/ ")
                print("      |  ")
                print("       \ ")
             if turns == 3:
                print("You have 3 turns left")
                print("---------")
                print("      O  ")
                print("     \|/ ")
                print("      |  ")
                print("     / \ ")
             if turns == 2:
                print("You have 2 turns left")
                print("---------")
                print("      O_ ")
                print("     \|/ ")
                print("      |  ")
                print("     / \ ")
             if turns == 1:
                print("You have 1 turns left")
                print("---------")
                print("      O_|")
                print("     \|/ ")
                print("      |  ")
                print("     / \ ")
             if turns == 0 :
                print("You loose")
                print("---------")
                print("      O_|")
                print("     /|\ ")
                print("      |  ")
                print("     / \ ")
                break
name= input("Enter your name: ")
print("Welcome",name,"!!")
print("Good luck, try to find the correct word")
hangman()