
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
    y = list(x)
    for i in range(len(y)):
        if i < len(y) - 1:
            if y[i] % 2 == 0:
                del y[i]
        else:
            if y[i] % 2!= 0:
                del y[i]
    return sorted(y)

