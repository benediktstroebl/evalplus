
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
    
    # lst1_len = 0
    # lst2_len = 0
    # for item in lst1:
    #     lst1_len += len(item)
    # for item in lst2:
    #     lst2_len += len(item)
    # if lst1_len < lst2_len:
    #     return lst1
    # elif lst2_len < lst1_len:
    #     return lst2
    # else:
    #     return lst1

    lst1_len = sum(len(i) for i in lst1)
    lst2_len = sum(len(i) for i in lst2)
    return lst1 if lst1_len < lst2_len else lst2

