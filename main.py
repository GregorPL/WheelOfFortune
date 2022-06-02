import random
import time

def game_options(options):
    i = 1

    for option in options:
        print(f"{i}. {option.capitalize()}")
        i += 1

values = [("100", 5), ("200", 5), ("500", 3), ("1000", 1), ("Bankrut", 2), ("Graj dalej", 1)]

values_on_wheel = []

for value in values:
    for i in range(value[1]):
        values_on_wheel.append(value[0])

player = str(input("Hello in 'Wheel of Fortune' game! Whats your name?"))

print(f"Ok {player}, lets start!")

while True:
    input("Please spin the wheel.")

    print("Wheel is spinning...")
    
    time.sleep(2)

    current_value = random.choice(values_on_wheel)

    game_options(["Podaj spółgłoskę.", "Wykup samogłoskę."])

    print(f"Wheel stop on: {current_value}")