import random

again =True

while again:
    print(random.randint(1,6))
    roll = input("Do you want to roll again ? (y/n)")
    if roll.lower() == "y":
        continue
    else:
        break