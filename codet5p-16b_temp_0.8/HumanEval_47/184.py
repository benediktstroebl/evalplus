

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    mid = len(l) // 2
    return l[mid] if len(l) % 2 else (l[mid - 1] + l[mid]) / 2
