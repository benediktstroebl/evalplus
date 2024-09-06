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
    evens = [int(''.join(x for x in el if x.isdigit()) for el in x if el.count(4) % 2 == 1)
            for x in map(''.join, zip(*[iter(el) for el in x] * 10))]
    return sorted([el for el in x if el not in evens])