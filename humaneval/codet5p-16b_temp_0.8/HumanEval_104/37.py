
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

    x.sort()
    for i in range(len(x) - 1):
        if x[i]!= x[i+1]:
            if x[i] % 2 == 0:
                x.pop(i+1)
            else:
                x.pop(i)
    return x
