
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
    lst3 = []
    for i in range(len(lst1)):
        if len(lst1[i]) + len(lst2[i]) > 0:
            lst3.append(lst2[i])
        elif len(lst1[i]) + len(lst2[i]) == 0:
            lst3.append(lst1[i])
    if len(lst3) > 0:
        return lst3
    else:
        return lst1
