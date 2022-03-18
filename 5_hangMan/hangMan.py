import random
from words import words
import string




def get_valid_word(word):
    word = random.choice(words) 
    while '-' in word or ' ' in word: 
        word = random.choice(words)

    return word.upper() #stops itterating and then we will get a word that does not have a space or a dash

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keep track of what user has guessed
    lives = 6
    #geting user input
    while len(word_letters) > 0 and lives > 0:

        #letters user already used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #current word 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) #add to used letters..
            if user_letter in word_letters: # if the letter guessed is in word
                word_letters.remove(user_letter) #everytime I guess correctly then this word letter will just keep track of all the letters in a word
            else:
                lives = lives  - 1 #takes away a life when wrong
                print('Oopsies! Your letter is not in the word.') #notification of the mistake

        elif user_letter in used_letters: #and then if this user letter is, what the user just entered
            print('You have already used that character. Please try again.') #then that means they already used it before and it is an invalid guess. so we are going to print something

        else: #if they typed something thats not in the alphabet and is not in the used letters theyve already guessed
            print('Invalid character. Please try again.') #that just means that they typed in wrong character.Create an error message

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

hangman()