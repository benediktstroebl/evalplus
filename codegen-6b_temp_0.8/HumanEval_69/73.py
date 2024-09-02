
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
    h = {}
    for i in lst:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1
    print(h)
    mx = max(h.values())
    for i in h:
        if h[i] >= i and h[i] > mx:
            mx = h[i]
    return mx if mx > 0 else -1
