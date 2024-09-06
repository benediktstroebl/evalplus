
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
    l = {}
    for i in lst:
        if i in l.keys():
            l[i] += 1
        else:
            l[i] = 1
    
    max_freq = 0
    max_val = -1
    for i,j in l.items():
        if j >= i:
            if max_freq < j:
                max_freq = j
                max_val = i
    return max_val
