
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
    y = []
    while len(x) != 0:
        z = x.pop()
        for i in str(z):
            if i in '2468':
                break
        else:
            y.append(z)
    return sorted(y)
