

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    len_ = len(l)
    return l[len_ // 2] if len_ % 2 else (l[len_ // 2] + l[(len_ // 2) - 1]) / 2

