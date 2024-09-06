

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # filter(function, iterable)
    # filter =  filter(lambda x: x >= 0, [3, -4, 5, -5, 6, -6])
    # filter =  filter(lambda x: x >= 0, [3, -4, 5, -5, 6, -6])
    return filter(lambda x: x >= 0, l)

