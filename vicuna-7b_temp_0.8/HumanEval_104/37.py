
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
    for i in range(1, len(x)):
        for j in range(i):
            if (x[i] % 2 != 0 and x[j] % 2 != 0 and x[i] < x[j]):
                x.remove(x[i])
                x.remove(x[j])
    return x
