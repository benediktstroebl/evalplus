
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
    # Method 1
    # return sorted(list(set(x) - set(map(int, filter(lambda d: int(d)%2 != 0, str(x))))))
    # Method 2
    return sorted(list(set(x) - set(map(int, filter(lambda d: d%2 != 0, str(x))))))

