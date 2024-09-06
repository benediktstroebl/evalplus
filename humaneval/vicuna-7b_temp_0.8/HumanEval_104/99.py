
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
    i = 0
    while i < len(x) - 1:
        j = i + 1
        while j < len(x) and x[j] % 2 == 0:
            j += 1
        if j > i:
            x[i], x[j] = x[j], x[i]
            i += 1
    return x
