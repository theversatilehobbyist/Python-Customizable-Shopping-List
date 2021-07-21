print("Welcome to Shopping List!")
print("Press 1 to view your shopping list")
print("Press 2 to add an item into your shopping list")
print("Press 3 to delete an item from your shopping list")
print("Press 4 to exit the shopping list")
print("If your shopping list looks like this : [''], that means it is empty.")

placeholder = ""
shoppingList = [placeholder]

#While loop
while True:
    #Question
    answer = int(input("What would you like to do? "))

    #If the answer is 1 then print out the shoppingList
    if answer == 1:
        print(shoppingList)

    elif answer == 2:
        option = input("Would you like to add one item add a time or several items? Press o for one at a time and s for several items at a time. ")
        if option == "o":
            itemadd = input("What would you like to add? ")
            shoppingList.append(itemadd)
            print("Updated! Press 1 to view")
        elif option == "s":
            several = input("What items would you like to add? Separate your items with a space. ")
            var = several.split()
            shoppingList.append(var)
            print(var)
            print("Updated! Press 1 to view")

    elif answer == 3:
        print(shoppingList)
        item = input("Which item do you choose? Type in the number")
        if item == shoppingList.index(itemadd):
            print("I got in!")
            shoppingList.remove(item)
            print("Updated! Press 1 to view")


    elif answer == 4:
        print("Thank you for using Shopping List! See you next time!")
        break
