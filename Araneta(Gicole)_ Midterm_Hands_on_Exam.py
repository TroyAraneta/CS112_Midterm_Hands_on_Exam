import random

while True:
    random_num1 = random.randint(1, 99)
    random_num2 = random.randint(1, 99)
    random_symbol = random.randint(0, 3)
    symbols = ["+", "-", "×", "÷"]
    symbols2 = {"+": "+",
                "-": "-",
                "×": "*",
                "÷": "/"}

    if random_symbol == 3 and random_num1 < random_num2:
        continue

    correct_answer = eval(f"{random_num1} {symbols2[symbols[random_symbol]]} {random_num2}")

    guess_answer = int(input(f"What is {random_num1} {symbols[random_symbol]} {random_num2}? "))

    user_answer = round(guess_answer, 1)
    if user_answer == correct_answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

    again = input("Do you want to try again? [Y/N]: ").upper()
    if again == 'N':
        break
    else:
        print("")
        continue
