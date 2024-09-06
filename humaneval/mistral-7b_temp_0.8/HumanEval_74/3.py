
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
    #sorting both the lists according to the length of the strings and then comparing the values

    #solution 1
    # lst1.sort(key=len)
    # lst2.sort(key=len)
    # if len(lst1) == len(lst2):
    #     return lst1
    # else:
    #     return lst2

    #solution 2
    lst1.sort(key=len)
    lst2.sort(key=len)
    if len(lst1) == len(lst2):
        return lst1 if lst1 < lst2 else lst2
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
