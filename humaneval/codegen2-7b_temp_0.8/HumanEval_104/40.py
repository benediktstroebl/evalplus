
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
    
    if len(x) == 1:
        return x
    
    new_x = []
    for y in x:
        if y % 2 == 1:
            new_x.append(y)
    return sorted(new_x)
