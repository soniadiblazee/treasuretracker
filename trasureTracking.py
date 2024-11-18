# empty list and empty dictionary for player use

treasure = []
inv = {}


while True:
    print("\nchoose an option:")
    print("1 find/get a treasure")
    print("2 update inventory")
    print("3 display inventory")
    print("4 quit")

    choice = input("enter your choice: ")

if choice == "1":
    name = input("treasure name: ")
    quantity = int(input("enter quantity: "))
    value = int(input("value per unit: "))
    treasures.append(name)
    invetory[name] = {"quantity":quantity,"value per unit": value}
    print(f"{name} added to your invetory")
elif choice == "2":
    name = input("name of tyreasure to update: ")
    if name in invetory:
        new_quantity = int(input("enter the new quantity: "))
        value = int(input("enter the new value per unit: "))
        inventory[name]["quantity"] = new_quantity
        inventory[name]["value per unit"] = new_value
        print(f"{name} updated in your inventory")
    else:
        print("Treasure not found in inventory")
elif choice == "3":
    for item, details in inventory.items():
        print(f"name: {item}, quantity: {details['quantity']}, value per unit: {details['value per unit']}")
elif choice == "4":
    print("Good luck on your quest!")
else:
    print("Invalid choice. Please try again.")