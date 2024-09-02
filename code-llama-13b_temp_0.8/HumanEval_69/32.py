
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
    d = dict()
    for e in lst:
        d[e] = d.get(e, 0) + 1
    maxx = 0
    for i in d:
        if d[i] >= i and i > maxx:
            maxx = i
    return maxx if maxx != 0 else -1
    
    
