import random

def guess(x):
	random_number = random.randint(1, x)
	guess = 0 
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		if guess < random_number: #less than <
			print('Sorry, guess again. Too low.')
		elif guess > random_number: #more than >
			print('Sorry, guess again. Too high.')
	print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
	low = 1
	high = x
	feedback = '' 
	print(feedback)
	while feedback != 'c' and low != high:
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()

		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1
	print(f'Yay the computer guessed your number, {guess}, correctly!!')
computer_guess(100)


##the computer is literally talking to me thats wow
#if feedback is 'h' string then minus the high guess by 1,
#if the feedback is 'l' low string, make the low guess +1,
#those codes run in an if and elif
#high is being manipulated, low is being manipulated via guess, guess is a new variable
#guess has low and high passed in it
##if low does not equal high, which it doesnt, low does not equal high
#this is so friggin cool
