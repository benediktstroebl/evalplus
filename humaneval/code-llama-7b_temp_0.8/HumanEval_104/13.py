
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
    # My solution
    # return [x for x in x if not 2 in map(int, str(x))]

    # My solution 2
    return list(filter(lambda n: not 2 in map(int, str(n)), x))

