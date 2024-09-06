
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
    from operator import attrgetter
    from collections import defaultdict
    d = defaultdict(list)
    for digit in map(lambda x: int(str(x)), x):
        d[digit % 2].append(x)
    return sorted(d[0] + d[1], key=attrgetter('__index__'))

