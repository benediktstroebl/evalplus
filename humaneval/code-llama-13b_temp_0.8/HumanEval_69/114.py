
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
    m = {}
    for i in lst:
        m[i] = m.get(i, 0) + 1
    return max([k for k,v in m.items() if v >= k] + [-1])
    
    # Other solution:
    # return max((i for i, j in m.items() if j >= i), default=-1)
    
    # Other solution:
    # return max(i for i in lst if lst.count(i) >= i) or -1
