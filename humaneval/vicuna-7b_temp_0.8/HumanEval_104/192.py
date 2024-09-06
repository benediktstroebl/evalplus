
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
    x.sort()
    while x:
        for i in range(1, len(x)):
            if (x[i] % 2 == 0) and (x[i-1] != x[i] // 2):
                x.remove(x[i])
            elif (x[i] % 2 != 0) and (x[i-1] == x[i] // 2):
                x.remove(x[i])
        x = x[:-1]
    return x
