

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) % 2 == 0:
        n = len(l) // 2
        x = (l[n - 1] + l[n]) / 2
        return x
    else:
        n = len(l) // 2
        x = l[n]
        return x