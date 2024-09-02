
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
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)

    if len_lst1 == len_lst2:
        return lst1
    
    elif len_lst1 > len_lst2:
        return [lst for lst in lst1 if len(lst) < len(lst2)]
    
    else:
        return [lst for lst in lst2 if len(lst) < len(lst1)]



    # lst2 = lst2 or []
    # lst1 = lst1 or []

    # c1 = len(lst1)
    # c2 = len(lst2)

    # if c1 < c2:
    #     return [lst for lst in lst1 if len(lst) < c2]
    # elif c1 > c2:
    #     return [lst for lst in lst2 if len(lst) < c1]
    # else:
    #     return lst1

    # return [lst for lst in lst1 if len(lst) < len(lst2)]




