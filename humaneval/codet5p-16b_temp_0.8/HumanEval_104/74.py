
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

    x = list(map(str, x))
    x = list(map(lambda x: ''.join(i for i in x if i.isdigit()), x))
    x = list(filter(lambda x: int(x) % 2 == 0, x))
    return sorted(list(set(x)))


