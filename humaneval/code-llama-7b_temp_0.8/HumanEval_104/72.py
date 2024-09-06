
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
    x.sort()
    for i in x:
        for j in str(i):
            if j != '0' and j != '2' and j != '4' and j != '6' and j != '8':
                a.append(i)
    return a
