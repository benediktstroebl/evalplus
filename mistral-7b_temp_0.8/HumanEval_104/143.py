
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

    l = []
    for i in x:
        t = 0
        for j in str(i):
            if j%2 == 0:
                t += 1
        if t == 0:
            l.append(i)
    l.sort()
    return l




