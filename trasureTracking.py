# empty list and empty dictionary for player use

treasure = []
inv = {}

while True:
    print("\nChoose an option:")
    print("1. Add a treasure")
    print("2. Update inventory")
    print("3. Display inventory")
    print("4. Quit")

    choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter the name of the treasure: ")
    quantity = int(input("Enter the quantity: "))
    value = int(input("Enter the value per unit: "))
    
    treasures.append(name)
    inventory[name] = {"quantity": quantity, "value_per_unit": value}
    print(f"{name} added to your inventory.")
elif choice == "2":
    name = input("Enter the name of the treasure to update: ")
    if name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        new_value = int(input("Enter the new value per unit: "))
        inventory[name]["quantity"] = new_quantity
        inventory[name]["value_per_unit"] = new_value
        print(f"{name} updated in your inventory.")
    else:
        print("Treasure not found in inventory.")
elif choice == "3":
    for item, details in inventory.items():
        print(f"Name: {item}, Quantity: {details['quantity']}, Value per Unit: {details['value_per_unit']}")
# Exit Condition:
# Allow the user to quit the loop when they’re done.
elif choice == "4":
    print("Good luck on your quest!")
else:
    print("Invalid choice. Please try again.")
