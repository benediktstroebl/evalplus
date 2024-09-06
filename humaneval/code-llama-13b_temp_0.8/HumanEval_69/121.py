
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    if lst == []:
        return -1
    if len(lst) == 1:
        return lst[0] if lst[0] > 1 else -1
    f = {}
    for i in lst:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    max_f = 0
    res = 0
    for key, val in f.items():
        if key > max_f:
            max_f = key
            res = key
        if key > val and key > res:
            res = key
    return res

