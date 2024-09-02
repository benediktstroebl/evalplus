
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
    i = 0
    max_val = 0
    max_freq = 0
    
    for x in lst:
        if x > 0:
            val = x
            freq = lst.count(x)
            max_val = max(max_val, val * freq)
            max_freq = max(max_freq, freq)
    
    if max_freq >= val:
        return max_val
    else:
        return -1

lst = [4, 1, 2, 2, 3, 1]
result = search(lst)
