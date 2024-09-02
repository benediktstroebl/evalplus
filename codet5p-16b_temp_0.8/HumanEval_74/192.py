
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

    totals = []
    for s in lst1:
        total = 0
        for i in s:
            total += 1
        totals.append(total)
    for s in lst2:
        total = 0
        for i in s:
            total += 1
        totals.append(total)
    lowest = totals[0]
    for i in totals:
        if i < lowest:
            lowest = i
    lst = []
    for s in lst1:
        if len(s) <= lowest:
            lst.append(s)
    for s in lst2:
        if len(s) <= lowest:
            lst.append(s)
    return lst

