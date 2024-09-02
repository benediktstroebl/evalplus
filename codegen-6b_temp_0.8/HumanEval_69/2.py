
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
    freq_map = {}
    max_int, max_freq, result = None, 0, None
    for elem in lst:
        if not elem in freq_map:
            freq_map[elem] = 1
        else:
            freq_map[elem] += 1
        if freq_map[elem] > max_freq:
            max_freq = freq_map[elem]
            max_int = elem
        if max_freq == max_int:
            result = max_int

    return result
