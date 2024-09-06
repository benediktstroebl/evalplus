
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


    if len(lst1) + len(lst2) == 0:
        return []
    else:
        new_lst = lst1[:]

    while len(lst1) > 0 and len(lst2) > 0:
        if len(lst1) >= len(lst2):
            if sum([len(x) for x in lst1]) > sum([len(x) for x in lst2]):
                new_lst = lst1[:]
            else:
                new_lst = lst2[:]
        else:
            if sum([len(x) for x in lst1]) > sum([len(x) for x in lst2]):
                new_lst = lst2[:]
            else:
                new_lst = lst1[:]

        lst1 = lst1[1:]
        lst2 = lst2[1:]

    return new_lst




