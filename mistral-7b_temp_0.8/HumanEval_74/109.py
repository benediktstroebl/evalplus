
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
    length1 = 0
    length2 = 0
    for i in lst1:
        length1 += len(i)
    for i in lst2:
        length2 += len(i)
    if length1 == length2:
        for i in lst1:
            lst3.append(i)
        return lst3
    elif length1 < length2:
        for i in lst2:
            lst3.append(i)
        return lst3
    elif length1 > length2:
        for i in lst1:
            lst3.append(i)
        return lst3
