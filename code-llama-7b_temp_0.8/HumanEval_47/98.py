

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    midpoint = (len(l) - 1) // 2

    if len(l) % 2 == 0:
        return (l[midpoint] + l[midpoint + 1]) / 2
    else:
        return l[midpoint]


