
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
    # total_lst1 = []
    # total_lst2 = []
    # for a in lst1:
    #     for b in lst2:
    #         if a == b:
    #             total_lst1.append(a)
    # total_lst1 = list(set(total_lst1))
    # total_lst2 = list(set(total_lst2))
    # if len(total_lst1) >= len(total_lst2):
    #     return total_lst2
    # else:
    #     return total_lst1

    # total_lst1 = []
    # total_lst2 = []
    # for a in lst1:
    #     for b in lst2:
    #         if a == b:
    #             total_lst1.append(a)
    # total_lst1 = list(set(total_lst1))
    # total_lst2 = list(set(total_lst2))
    # if len(total_lst1) >= len(total_lst2):
    #     return total_lst2
    # else:
    #     return total_lst1

    total_lst1 = []
    total_lst2 = []
    for a in lst1:
        for b in lst2:
            if a == b:
                total_lst1.append(a)
    total_lst1 = list(set(total_lst1))
    total_lst2 = list(set(total_lst2))
    if len(total_lst1) >= len(total_lst2):
        return total_lst2
    else:
        return total_lst1
