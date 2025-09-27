# Variables
groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

shopping_cart = []

total = 0

# Filling the shopping cart 
user_choice = input("What do you want to buy? ")
item_data = user_choice.split(" ") 

while item_data[0] != "done":
    if item_data[0] in groceries:
        shopping_cart.append(item_data[0])
        total += groceries[item_data[0]] * int(item_data[1])
    else:
        print("Sorry, we don't have that item.")
    
    user_choice = input("What do you want to buy? ")
    item_data = user_choice.split(" ") 

print("You bought:", shopping_cart)
print("Total = $", total)
if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")