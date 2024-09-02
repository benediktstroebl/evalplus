
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
    lst1, lst2 = list(lst1), list(lst2)
    for i in lst1:
        total1 = 0
        for j in i:
            total1 += ord(j)
    for i in lst2:
        total2 = 0
        for j in i:
            total2 += ord(j)
    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1

