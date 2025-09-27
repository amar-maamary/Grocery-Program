# Variables
groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

shopping_cart = []

# Filling the shopping cart 
user_choice = input("What do you want to buy? ")

while user_choice != "done":
    if user_choice in groceries:
        shopping_cart.append(user_choice)
    else:
        print("Sorry, we don't have that item.")
    
    user_choice = input("What do you want to buy? ")

print("You bought:", shopping_cart)