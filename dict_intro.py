#Dictionaries

#Dictionaries are implemented as hash maps or hash tables with hash functions
#A dictionary is a pairing between the set of keys and the set of values
#Every entry in the dictionary is key : value pair.

phone_pair = {"Mia" : "555-424-3376"} #Value can be found with key but not vice versa, prior knowledge needed
print(phone_pair["Mia"])        #Looks up Mia's phone number
#print(phone_pair("555-424-3376")) (wont work, hashed out)

#Immutable vs. Mutable types
#Mutable data can be changed and often is in memory. A structured data list
#is a mutable data structure. Strings are immutable. When it looks like a 
#string is being changed, there is actually a new string object created and
#the old one is discarded.
#Username = " "
#Username = last + "_" + first[0]
#Username = Username + first[1]

#The keys of a dictionary have to be an immutable type. This is so that the
#hash function obtains the same value every time

#Empty dictionary
my_dict = {}

phone_list = {"Karthik" : "555-3691", "Jae" : "555-2211", "Kayoko" : "555-1133"}

print(phone_list.keys())
print(phone_list.values())

#Add to a dictionary

phone_list["Nisha"] = "222-3145"
print(phone_list)

phone_list["Karthik"] = "555-1313"
print(phone_list)

#Exercise for practice!!
def freq_count(phrase):
    '''
    Purpose: Count the number of occurences for each character in the phrase
    and return a dictionary with these counts
    
    Parameters: phrase - the phrase we are getting the frequency for; str
    
    Return value: A dictionary with a freq count for each character in the phrase
    '''

    char_count = {}
    for character in phrase:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count

def freq_count_words(phrase):
    '''Change freq_count so that it returns the frequency count of words in 
    the phrase instead of the characters.
    '''

    word_count = {}

    words = phrase.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

#write a function

def classList(students, year):
    '''
    Purpose: To take a dictionary students with student : grad year pairs
    and produce a list with students who graduate in the parameter year.
    
    Parameters:
        students - a dictionary with name as keys and class year as values; dict
        year - the year that the students are graduating; int
        
    Return value: List of students who are graduating in the year; list
    '''

    Examples:
        >>> student_list = ["Datu" : 2027, "Pavi" : 2030, "Melissa" : 2029, "Molin" : 2030]

    names = []

    for person in students:
        if students[person] == year:
            names.append(person)



if __name__ == "__main__":
    print(freq_count_words("Today is my birthday and I am turning sixteen!!!"))
