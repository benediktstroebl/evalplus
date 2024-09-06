
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
    match = []
    l1 = len(lst1)
    l2 = len(lst2)
    if l1 > l2:
        for i in range(l2, l1):
            if lst1[i] in lst2:
                match.append(lst1[i])
        return match
    else:
        for i in range(l1):
            if lst2[i] in lst1:
                match.append(lst2[i])
        return match
