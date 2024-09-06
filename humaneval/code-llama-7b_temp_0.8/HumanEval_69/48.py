
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
    if len(lst) == 0:
        return -1
    vals = {}
    for val in lst:
        if val not in vals:
            vals[val] = 1
        else:
            vals[val] += 1

    for val in vals:
        if vals[val] >= val and val > 0:
            return val
    return -1

