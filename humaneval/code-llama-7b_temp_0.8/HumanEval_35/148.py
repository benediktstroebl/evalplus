

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        raise ValueError('Cannot get max of an empty list.')

    max_ = l[0]
    for e in l:
        if e > max_:
            max_ = e
    return max_

