
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
    # first_total = 0
    # for item in lst1:
    #     first_total += len(item)
    # second_total = 0
    # for item in lst2:
    #     second_total += len(item)
    # if first_total < second_total:
    #     return lst1
    # else:
    #     return lst2
    first_total = sum([len(item) for item in lst1])
    second_total = sum([len(item) for item in lst2])
    if first_total > second_total:
        return lst1
    elif first_total < second_total:
        return lst2
    else:
        return lst1
    
