

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_copy = sorted(l)
    if len(l_copy) % 2 == 0:
        return (l_copy[len(l_copy) // 2] + l_copy[len(l_copy) // 2 - 1]) / 2
    return l_copy[len(l_copy) // 2]
