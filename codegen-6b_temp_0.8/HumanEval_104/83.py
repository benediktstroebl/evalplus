
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    unique = []
    for x in x:
        '''
        if x % 2 == 0:
            continue
        '''
        if not any(int(digit) % 2 == 0 for digit in str(x)):
            unique.append(x)
    return sorted(unique)


from timeit import Timer
