
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
    # note: the above comments are not from the Udacity assessment
    
    # 's' is the set of lst, with each element as a tuple
    s = set([(x, lst.count(x)) for x in lst])
    for x,f in s:
        if x > 0 and f >= x:
            return x
    return -1
