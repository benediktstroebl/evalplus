

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    if len(l) <= 1:
        return l
    else:
        if l[0] > 0:
            return [l[0]] + get_positive(l[1:])
        else:
            return get_positive(l[1:])
