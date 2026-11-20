#Tuples

#Tuples are an ordered immutable sequence. The looked like ordered tuples
#In mathematics - (1, 2-1), ("a", "b", "c")

#create an empty tuple
point = tuple()
point = ()

print(type(point))

point = (2)
print(type(point))
point = (2,)
print(type(point))

#concatenate tuples
point = point + (-3, 5)
print(point)

#Tuple unpacking
x, y, z = point
print(f"x: {x}, y:{y}, z:{z}")

# x, y = point (there are too few items we r calling)
#x, y, z, w = point (there are too mant items we r calling)

#Ignore entries in a tuple with an underscore
x, y, _ = point
print(f"x:{x}, y:{y}")

#We can index tuples
print(point[2])

#Tuples are immutable so you can't change individual items
#point[2] = 0

#Exchange the values in 2 variables

a = 5
b = -7

#Swapping with tuples
value_tuple = (a,b)
b, a = value_tuple

b, a = a, b     #The short way to swap

#Swap without tuples
temp = a
a = b
b = temp

#Return multiple items out of a function
algebra_scores = [88, 95, 70, 62, 99, 24, 74, 85]
def find_max_min(scores):
    '''
    Purpose: Find the maximum and the minimum items in a list
    Parameters: score - the numerical list of scores we want the max/min
    for; list
    Return values: max, min; float/int
    '''

    maximum = scores[0]
    minimum = scores[0]
    for item in scores:
        if item > maximum:
            maximum = item
        if item < minimum:
            minimum = item
    
    return maximum, minimum

#print(find_max_min(scores)) (one way to do it)
big, little = find_max_min(algebra_scores)
print(f"Maximum: {big}, Minimum: {little}")

#Exercise!!!

my_rocks = [('talc', 1), ('lead', 1.5), ('copper', 3), ('nickel', 4), \
         ('silicon', 6.5), ('emerald', 7.5), ('boron', 9.5), ('diamond', 10)]

#The first element of each tuple is the mineral and the second is its hardness rating
#Soft = 1-3
#Medium = 3.1-5
#Hard = 5.1-8
#Very hard = 8.1-10

def hardness(rocks):
    '''
    Purpose: To take a list of (mineral, hardness) and make a dictionary of
    hardness categories
    Parameters: rocks is a list of tuples of minerals and hardness ratings
    Return value: dictionary where the hardness categories are the keys and
    the values are a list of minerals for that category
    
    Example:
        >>> hardness(my_rocks)
        {'soft': ['talc', 'lead', 'copper],
        'medium': ['nickel'],
        'hard: ['silicon', 'emerald'],
        'very hard': ['boron', 'diamond']}
    '''

    category_dict = {'soft': [], 'medium':[], 'hard': [], 'very hard': []}

    for item in rocks:
        if item[1] > 8:
            category_dict['very hard'].append(item)
        elif item[1] > 5:
            category_dict['hard'].append(item)
        elif item[1] > 3:
            category_dict['medium'].append(item)
        else:
            category_dict['soft'].append(item)

    return category_dict


#advantages of tuples
#tuples use less space than lists
#you can't change tuples by mistake
#You can use tuples are dictionary keys
#function arguments are passed as tuples
#return more than one item out of a function using tuples.