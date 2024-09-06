
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
    freq = {}
    for i in lst:
        freq[i] = freq.get(i,0) + 1
    max_freq = 0
    max_val = None
    for i in freq:
        if freq[i] > max_freq:
            max_freq = freq[i]
            max_val = i
    return max_val if max_freq >= max_val else -1
