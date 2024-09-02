
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
    if not lst1:
        return []
    if not lst2:
        return []
    
    t1, t2 = 0, 0
    for el1 in lst1:
        t1 += len(el1)
    for el2 in lst2:
        t2 += len(el2)
    
    if t1 < t2:
        return lst1
    elif t2 < t1:
        return lst2
    else:
        return lst1

