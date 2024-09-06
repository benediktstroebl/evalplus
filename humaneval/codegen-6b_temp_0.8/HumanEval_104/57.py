
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
    # return list(set([str(x) for x in x if len([i for i in str(x) if i in '02468'] ) < 2]))
    # return sorted(list(set([str(x) for x in x if len([i for i in str(x) if i in '02468']) < 2])))
    return sorted([str(x) for x in x if len([i for i in str(x) if i in '02468']) < 2])

