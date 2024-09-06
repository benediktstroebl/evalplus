
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
    
    if len(x) == 0:
        return []
    
    # filter x to get only the numbers that have no even digits
    # then sort the resulting list
    return sorted([i for i in x if all(d % 2 == 1 for d in str(i))])
