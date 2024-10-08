

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) % 2 == 1:
        return sorted(l)[len(l) // 2]
    else:
        return (sorted(l)[len(l) // 2 - 1] + sorted(l)[len(l) // 2]) / 2

