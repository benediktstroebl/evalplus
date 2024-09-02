
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
    d = [0] * 10
    for i in x:
        while i != 0:
            d[i % 10] += 1
            i //= 10
    r = []
    for i in range(10):
        if d[i] == 1 and i % 2 != 0:
            r.append(i)
    return sorted(r)


