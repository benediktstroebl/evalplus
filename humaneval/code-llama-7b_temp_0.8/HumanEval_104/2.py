
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

    # Solution 1
    # return sorted(list(set([x for x in x if not any(y in str(x) for y in '2468')])))

    # Solution 2
    # return sorted(list(set([int(''.join(filter(lambda x: x not in '2468', str(i)))) for i in x])))

    # Solution 3
    return sorted(list(set([int(''.join(filter(lambda x: x not in '2468', str(i)))) for i in x if not any(y in str(i) for y in '2468')])))

