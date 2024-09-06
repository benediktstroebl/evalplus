
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
    n_digits = len(str(x))
    all_digits = [digit for digit in range(10) if digit < n_digits]
    return [x for x in xrange(1, x+1) if len([digit for digit in str(x) 
                                              if int(digit) % 2 == 0]) % 2 == 1]
