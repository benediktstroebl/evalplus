
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

    # total_lst = []
    # for item in lst1:
    #     for item2 in lst2:
    #         if len(item) < len(item2):
    #             total_lst.append(item)
    #             break
    #         elif len(item2) < len(item):
    #             total_lst.append(item2)
    #             break
    #         else:
    #             continue
    
    # return total_lst

    total_lst = []
    for item in lst1:
        for item2 in lst2:
            if len(item) == len(item2):
                total_lst.append(item)
                total_lst.append(item2)
            elif len(item) < len(item2):
                total_lst.append(item)
            elif len(item2) < len(item):
                total_lst.append(item2)
            else:
                continue
    
    return total_lst
