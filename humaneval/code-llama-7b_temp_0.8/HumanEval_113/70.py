
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
    # My solution
    lst2 = []
    for i in range(len(lst)):
        lst2.append(lst[i].count('1')+lst[i].count('3')+lst[i].count('5')+lst[i].count('7'))
    lst3 = []
    for i in range(len(lst)):
        lst3.append("the number of odd elements " + str(lst2[i]) + "n the str" + str(i+1) + "ng " + str(i+1) + " of the " + str(i+1) + "nput.")
    return lst3

    # Not mine
    lst3 = []
    for index, item in enumerate(lst):
        lst3.append("the number of odd elements " + str(len(item.count('1')+item.count('3')+item.count('5')+item.count('7'))) + "n the str" + str(index+1) + "ng " + str(index+1) + " of the " + str(index+1) + "nput.")
    return lst3


