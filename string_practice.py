phrase = "Robots are the best!"

#print the first character of the phrase
print(phrase[0])
print(phrase[-len(phrase)])

#print the length of the phrase
print(len(phrase))

#if we try to print what is at index 20, (there is none; goes 0-19)
#print(phrase[20])

#print the last character of the phrase
print(phrase[-1])
print(phrase[len(phrase)-1])


#special characters
#escape characters
# \t = tab
# \n = newline
# \\ = backslash
# \" = quote
# \' = apostrophe

wish = " My first class starts at: \t 11am"
lunch_main = "Steak"
lunch_side = "Fries"
lunch_drink = "Water"
lunch_dessert = "Cake"
lunch_after = "Ice cream"

print(lunch_main, end="\t")
print(lunch_side, end="\t")
print(lunch_drink, end=",\t")
print(lunch_dessert, end=" $4.75\n")
print(lunch_after)
print(wish)

# Fstrings allow us to fill-in-the-blank in a nice way

lunch_order = f"My lunch order is: {lunch_main}, \t {lunch_side}, \t {lunch_drink}, "
dessert_order = f"For dessert: {lunch_dessert}, \t Cost: ${4.7536:.2f}"


print (lunch_order)
print(dessert_order)

# String methods
print(wish.strip())   #strip() gets rid of white space at the beginning
                        # of a string

wish_list = wish.split()    #split creates a list from wish by splitting
print(wish_list)            #on spaces by default

# comma separated values (CSV)
lunch = "sandwich, chips, cauliflower, soda"
lunch_list = lunch.split(",")
print(lunch_list)

def strip_list(list_items):
    '''
    Purpose: to strip any whitespace at the beginning and end of each
    item in list_items

    Parameters: list_items - the list of itens to be stripped of white space; list str

    Return value; list_items with the white space removed; list str
    '''

    for index in range(len(list_items)):
        list_items[index] = list_items[index].strip()


    return list_items

print(strip_list(lunch_list))

#Slicing is to get substrings or subsequences 
#String_var[start : stop : skip]
#start is inclusive, stop is exclusive and skip is how many steps to take

print(wish[2:6])    #start at index 2 and end at index 5
print(wish[:6])     #start at index 0 and end at index 5
print(wish[3:])     #start at index 3 and finish
print(wish[:8:3])   #write every 3rd character from index 0-7

print(wish[::-1])   # prints in reverse