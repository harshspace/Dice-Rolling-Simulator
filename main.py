import numpy as np
print("Wellcome to Dice Rolling Simulator")
while True:
    rand = np.random.randint(1,7)
    print("dice no is",rand)
    y = input("you want to role again press yes ")
    if y == 'yes':
        print("Wellcome to Dice Rolling Simulator ")
    else:
        break
print("Thank you to participate")