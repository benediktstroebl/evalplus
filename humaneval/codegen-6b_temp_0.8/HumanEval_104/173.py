
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
    # only need to compare to last number
    # since we know the numbers will be sorted incrementally
    x = sorted(x)
    for i in range(0, len(x)-1):
        if x[i] % 2 == 0:
            x[i] += 1
    return x

