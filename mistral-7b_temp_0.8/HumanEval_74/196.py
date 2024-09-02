
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
    res = []
    total = 0
    if len(lst1) > len(lst2):
        total = len(lst1)
    else:
        total = len(lst2)

    for i in lst1:
        total += len(i)

    for i in lst2:
        total += len(i)
    print(total)

    for i in lst1:
        if len(i) < total:
            res.append(i)

    for i in lst2:
        if len(i) < total:
            res.append(i)

    res.sort()
    return res
