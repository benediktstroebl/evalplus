
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
    lst1 = sorted(lst1, key = len)
    lst2 = sorted(lst2, key = len)
    len1 = len(lst1)
    len2 = len(lst2)
    if len1 == len2:
        return lst1
    elif len1 > len2:
        lst = lst1[len1 - len2:]
    else:
        lst = lst2[len2 - len1:]
    return lst


