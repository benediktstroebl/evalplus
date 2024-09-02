
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
    if len(lst1) > len(lst2):
        return lst1
    elif len(lst1) < len(lst2):
        return lst2
    lst1total = 0
    lst2total = 0
    for string in lst1:
        lst1total += len(string)
    for string in lst2:
        lst2total += len(string)
    if lst1total < lst2total:
        return lst1
    else:
        return lst2


