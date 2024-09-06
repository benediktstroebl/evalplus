
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
    # filter to get only those number that don't have even digits
    x_filtered = [x for x in x if not any(y for y in str(x) if int(y) % 2 == 0)]

    return sorted(x_filtered)



