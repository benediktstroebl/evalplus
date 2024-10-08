

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return len(l) % 2 == 0 and (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2 or l[len(l) // 2]

