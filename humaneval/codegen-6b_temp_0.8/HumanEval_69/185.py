
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
    max_val = 0
    max_freq = 0
    max_idx = -1
    for idx, val in enumerate(lst):
        freq = lst.count(val)
        if freq > max_freq:
            max_freq = freq
            max_idx = idx
            max_val = val
    return max_val, max_idx
