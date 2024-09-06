
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
    # your code here
    # if one of them is empty return the other list
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1

    # if they have the same size return the first list
    if len(lst1) == len(lst2):
        return lst1
    
    # if they have different sizes
    # initialize two vars
    count1 = 0
    count2 = 0
    # loop through each item of the first list and calculate the count
    for char in lst1:
        count1 += len(char)
    # loop through each item of the second list and calculate the count
    for char in lst2:
        count2 += len(char)
    # if count1 is less than count2 return the first list
    if count1 < count2:
        return lst1
    # else return the second list
    return lst2
