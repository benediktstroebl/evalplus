
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
    # My code
    lst = []
    if len(lst1) <= len(lst2):
        for i in range(len(lst1)):
            for j in range(len(lst1[i])):
                lst.append(lst1[i][j])
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                lst.append(lst2[i][j])
        total = 0
        for i in range(len(lst)):
            total += len(lst[i])
        if total >= 2 * len(lst1):
            return lst1
        elif total >= 2 * len(lst2):
            return lst2
        else:
            return lst1
    else:
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                lst.append(lst2[i][j])
        for i in range(len(lst1)):
            for j in range(len(lst1[i])):
                lst.append(lst1[i][j])
        total = 0
        for i in range(len(lst)):
            total += len(lst[i])
        if total >= 2 * len(lst2):
            return lst2
        elif total >= 2 * len(lst1):
            return lst1
        else:
            return lst2

    # Given Code
    if not lst1 or len(lst1) == 0:
        return lst2
    elif not lst2 or len(lst2) == 0:
        return lst1
    total1 = len(lst1[0])
    total2 = len(lst2[0])
    for i in range(1, len(lst1)):
        total1 += len(lst1[i])
    for i in range(1, len(lst2)):
        total2 += len(lst2[i])
    return lst1 if total1 < total2 else lst2

