import random


while True:
    maximum = int(input('Specify a maximum value: '))
    minimum = int(input('Specify a minimum value: '))
    number_to_guess = random.randint(minimum, maximum)

    while True:
        try:
            guess = int(
                input(f'Guess the number between {maximum} and {minimum}: '))
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
    choice = input('Play more? (y/n): ').lower()
    if choice != "y":
        print('Thank you for playing!')
        break
