
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
    n = len(lst)
    if n == 0:
        return -1
    i = 0
    max_value = 0
    max_freq = 0
    while i < n:
        value = lst[i]
        if value > 0:
            freq = lst.count(value)
            if freq >= value:
                max_value = max(max_value, value)
                max_freq = max(max_freq, freq)
            i += 1
    return max_value, max_freq

lst = [4, 1, 2, 2, 3, 1]
max_value, max_freq = search(lst)
