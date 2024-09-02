
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
    lst_1 = [i for i in lst1]
    lst_2 = [i for i in lst2]
    while len(lst_1) > len(lst_2):
        lst_1.pop()
    while len(lst_2) > len(lst_1):
        lst_2.pop()
    return lst_1 if sum(len(i) for i in lst_1) < sum(len(i) for i in lst_2) else lst_2
    '''
    '''
    result = []
    if len(lst1) > len(lst2):
        for i in lst2:
            if i in lst1:
                result.append(i)
    elif len(lst2) > len(lst1):
        for i in lst1:
            if i in lst2:
                result.append(i)
    else:
        for i in lst1:
            if i in lst2:
                result.append(i)
    return result
    '''
