import random, wordlist

words = wordlist.wordList()

# this is a comment

wordChoiceIndex = random.randint(0, len(words))
chosenWord = words[wordChoiceIndex]
# print(chosenWord)

counter = 0 

while counter < 6:

  print(" ")
  userGuessInput = input("Guess the word: ")
  counter+=1
  userGuess = list(userGuessInput)
  if userGuessInput in words:
    for i in range(len(userGuess)): #iterating through all characters in the guess
          
      if userGuess[i] == chosenWord[i]: #prints words as green if position is correct
        print("|", end="")
        print("\u001b[42m" , userGuess[i] , end="" )
        print("\u001b[0m|", end="")
            
      elif userGuess[i] in chosenWord: #printing character as yellow
        print("|", end="")
        print("\u001b[43;1m", userGuess[i], end="")
        print("\u001b[0m|", end="")

      else: #resets ANSI code to normal and prints letter
        print("|", end="")
        print("\u001b[0m", userGuess[i], end="")
        print("\u001b[0m|" , end="")
        i+=1

    if userGuessInput == chosenWord: #checking for wins
      print("")
      print("congratulations, you win!")
      break
  if userGuessInput not in words:
    print("the word is not in the list, try again")
    counter-=1

if counter >= 6:
  print(" ")
  print("you didn't guess it, you lose")
  print("the word was: " , chosenWord)

