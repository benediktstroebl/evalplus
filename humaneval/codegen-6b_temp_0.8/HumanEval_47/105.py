

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    p = len(l) // 2
    return l[p] if len(l) % 2 == 1 else (l[p - 1] + l[p]) / 2

