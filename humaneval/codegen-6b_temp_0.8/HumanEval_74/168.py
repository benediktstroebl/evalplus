
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
    lst1 = list(filter(None, lst1))
    lst2 = list(filter(None, lst2))
    total = 0
    lst = []
    if len(lst1) == len(lst2):
        return lst1
    for val in lst1:
        total += len(val)
    for val in lst2:
        total += len(val)
    if total < len(lst1) + len(lst2):
        return lst1
    return lst2


