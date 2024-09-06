
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
    ret = -1
    for i in lst:
        if ret < i and lst.count(i) >= i:
            ret = i

    return ret

assert search([4, 1, 2, 2, 3, 1]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([5, 5, 4, 4, 4]) == -1
assert search([1]) == -1
assert search([7, 1, 4, 1, 5, 3, 4, 1]) == -1
assert search([4, 1, 4, 1, 1, 3, 1, 1]) == 4