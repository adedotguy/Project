#linear search algorithms (searching one after another)
"This code returns the place of the number entered if it is in the list"
def linear_search (items, search_item):
    index = -1
    current = 0
    found = False
    
    #checks the length and item to be found

    while current < len(items) and found == False:
        if items[current] == search_item:
            index = current + 1
            found = True
        current = current + 1
    #This is to return the integer in the list
    return index

#Item and search term 

items = ["5", "3", "7", "3", "9", "10", "3", "2", "1", "11", "6", "7", "10", "11", "12", "13", "15", "20"]
search_item = input("Enter a number from the list: ")
print(linear_search(items, search_item))
