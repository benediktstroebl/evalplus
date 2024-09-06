
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # create a variable that will be the total number of chars in all strings in lst1
    total1 = 0
    # create a variable that will be the total number of chars in all strings in lst2
    total2 = 0
    
    # for every string in lst1, add the length of the string to the total1 variable
    for string in lst1:
        total1 += len(string)
        
    # for every string in lst2, add the length of the string to the total2 variable
    for string in lst2:
        total2 += len(string)
    
    # if the number of chars in lst1 are less than the number of chars in lst2, return lst1
    if total1 < total2:
        return lst1
    
    # if the number of chars in lst1 are greater than the number of chars in lst2, return lst2
    elif total1 > total2:
        return lst2
    
    # if the number of chars in lst1 are equal to the number of chars in lst2, return lst1
    elif total1 == total2:
        return lst1
