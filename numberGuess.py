import random
import time

# Input phase
smaller = input("Please enter the smaller number: ")

while not smaller.isdigit():
    smaller = input("Sorry, please enter a small DIGIT: ")

smaller = int(smaller)

larger = input("Now, please enter the larger number: ")

while not larger.isdigit():
    larger = input("Sorry, please enter a large DIGIT: ")

larger = int(larger)

# Processing phase
magicNum = random.randint(smaller, larger)
print("Selecting your magic number...")
time.sleep(3)

# Variable to track the number of attempts for the game
count = 0

# Loop to keep the game going until the number is guessed
while True:
    userNumber = input("Enter your guess: ")

    while not userNumber.isdigit():
        userNumber = input("Sorry, please enter a DIGIT for your guess: ")

    userNumber = int(userNumber)
    count += 1

    # Logic to determine the game outcome
    if userNumber < magicNum:
        print("Sorry, your guess was too SMALL!")
    elif userNumber > magicNum:
        print("Sorry, your guess was too LARGE!")
    else:
        print("Congratulations! You guessed it in", count, "tries!")
        break

# Output phase
input("Thank you for playing! Press ENTER to quit.")
