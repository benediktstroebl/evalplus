
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
    seen = set()
    seen_add = seen.add
    seen_lit = [x for x in range(10) if not x % 2]

    return [x for x in x if not any(map(lambda y: y in x, seen_lit)) and not x in seen_add(x)]
