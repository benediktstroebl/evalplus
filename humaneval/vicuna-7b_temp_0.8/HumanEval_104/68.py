
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
    x = list(x)
    while x:
        x1, x2 = x[:2], x[2:]
        for i in range(len(x1)):
            x1, x2 = x1[:2], x1[2:] + x2
            x2 = str(int(x2))
            if len(str(x2)) % 2 == 0:
                break
        else:
            x = x1
    return x
