
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """

    #Removing the dot
    lst1 = [element.replace(".","") for element in lst]

    #Creating a list of tuples
    lst2 = [(elem, elem.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")) for elem in lst1]

    #Getting the count of odd numbers
    lst3 = [("the number of odd elements in the string "+str(count)+" of the input.", elem[1].count("")) for count, elem in enumerate(lst2)]

    return lst3
