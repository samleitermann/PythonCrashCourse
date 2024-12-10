

ordering = True

print('What topping would you like to add to your pizza? When you are done adding toppings, type quit to exit.')

while ordering:

    topping = input("Topping: ")

    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza")


