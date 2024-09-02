
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

    if len(lst1) == len(lst2):
        return lst1
    elif len(lst1) > len(lst2):
        smaller_lst = lst2
    else:
        smaller_lst = lst1

    for i in range(0, len(smaller_lst)):
        smaller_lst[i] = len(smaller_lst[i])

    smaller_lst = sorted(smaller_lst)

    if len(lst1) > len(lst2):
        for i in range(0, len(lst1)):
            if len(lst1[i]) > smaller_lst[0]:
                lst1.remove(lst1[i])
    else:
        for i in range(0, len(lst2)):
            if len(lst2[i]) > smaller_lst[0]:
                lst2.remove(lst2[i])
    return lst1 if len(lst1) < len(lst2) else lst2
