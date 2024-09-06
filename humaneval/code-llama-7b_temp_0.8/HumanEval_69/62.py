
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
    _min = float('inf')
    _max = float('-inf')
    _freq = {}
    for n in lst:
        if n < 0:
            continue
        if n in _freq:
            _freq[n] += 1
        else:
            _freq[n] = 1
        if n > _max:
            _max = n
        if n < _min:
            _min = n

    for n, freq in _freq.items():
        if freq >= n:
            return n
    return -1

