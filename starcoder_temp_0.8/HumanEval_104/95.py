
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
    return sorted(set([x for x in x if len(str(x)) == len(list(filter(lambda y: y % 2 == 1, list(map(int, list(str(x)))))))]) - set([x for x in x if len(str(x)) == len(list(filter(lambda y: y % 2 == 0, list(map(int, list(str(x)))))))]))

