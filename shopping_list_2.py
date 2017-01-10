# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use  the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'SAVE' to save your current list.
""")

def show_list():
    # print out the list
    print("Here's your list:")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items".format(new_item, len(shopping_list)))

def save_to_list():
    # save the list
    file = input("Enter file name: ") + str(".txt")

    try:
        with open(file, 'w') as file:
            for items in shopping_list:
                file.write(str(items) + "\n")
    except:
        print("An error has occured.")

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    elif new_item == 'SAVE':
        save_to_list()
        print("List has been saved!")
        continue
    add_to_list(new_item)

show_list()
