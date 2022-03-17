import random

# def guess(x):
# 	random_number = random.randint(1, x)
# 	print(random_number)
# 	#too high or too low keep looping
# 	guess = 0 #why
# 	while guess != random_number:
# 		guess = int(input(f'Guess a number between 1 and {x}: '))
# 		if guess < random_number: #guess less than than random number
# 			print('Sorry, guess again. Too low.')
# 		elif guess > random_number:
# 			print('Sorry, guess again. Too high.')
# 	print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')


# guess(10)

def guess(y):
	x = 1
	random_number = random.randint(x, y)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between {x} and {y}: '))
		if guess < random_number:
			print('Sorry, guess again. Too low.')
		elif guess > random_number:
			print('Sorry, guess again. Too high.')
	print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')


guess(10)