
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
    if not lst:
        return -1
    res = {}
    for el in lst:
        if el in res:
            res[el] += 1
        else:
            res[el] = 1
    res = sorted(res.items(), key=lambda el: (el[1], el[0]), reverse=True)
    return res[0][0] if res[0][0] > 1 and res[0][1] >= res[0][0] else -1
