
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
    from operator import itemgetter
    from functools import reduce
    from string import digits
    return sorted(list(set(filter(lambda x: not any(map(lambda n: n in '2468', digits[1:])), x))))
