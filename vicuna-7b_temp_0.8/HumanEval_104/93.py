
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
    if not x:
        return []
    x = sorted(x)
    return [x[i] for i in range(1, len(x)) if not any(str(j) in str(x[i]) for j in [2, 4, 6, 8]) for j in [0, 1, 3, 5]]
