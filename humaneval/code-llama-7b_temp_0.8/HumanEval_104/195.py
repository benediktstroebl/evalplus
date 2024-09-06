
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
    if len(x) == 1:
        return [x[0]] if len(str(x[0])) > 1 and x[0] % 2 else []
    else:
        return unique_digits([i for i in x if len(str(i)) > 1 and i % 2])

