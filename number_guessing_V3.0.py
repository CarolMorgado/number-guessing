import random

number_of_guesses = 0

while True:
    maximum = int(input('Specify a maximum value: '))
    minimum = int(input('Specify a minimum value: '))
    number_to_guess = random.randint(minimum, maximum)

    for number in range(5):
        try:
            guess = int(
                input(f'Guess the number between {maximum} and {minimum} (5 attempts): '))
            number_of_guesses += 1
            if minimum <= guess <= maximum:
                if guess == number_to_guess:
                    print('Congratulations! You guessed the number!')
                    break
                elif guess < number_to_guess:
                    print('Too low!')
                else:
                    print('Too high!')
            else:
                print('Please enter a valid number!')

        except:
            print('Please enter a valid number!')

    if guess != number_to_guess:
        print(f'Correct number: {number_to_guess}')
    choice = input('Play more? (y/n): ').lower()
    if choice != "y":
        print('Thank you for playing!')
        break
