
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
    return sorted([n for n in x if not any([d%2 == 0 for d in map(int,str(n))])])
    
    # This one-liner works too!
    return sorted([x for x in x if not any([d%2 == 0 for d in map(int,str(x))])])

    # This is the most common solution.
    return sorted([n for n in x if not any(map(lambda d: d%2==0, map(int, str(n))))])

