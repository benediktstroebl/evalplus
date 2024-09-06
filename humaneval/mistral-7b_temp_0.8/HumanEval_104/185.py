
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
    a = []
    b = []
    for i in x:
        b.append(i)
    for i in range(len(b)):
        if (b[i] % 2 != 0):
            a.append(b[i])
    a.sort()
    return a

