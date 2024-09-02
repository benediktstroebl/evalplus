
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
    import math
    l = []
    for i in x:
        dig = []
        while i > 0:
            d = i%10
            if (d%2 != 0):
                dig.append(d)
            i = int(i/10)
        dig.sort()
        l.append(dig)
    return sorted(l)
