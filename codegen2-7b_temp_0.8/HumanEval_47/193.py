

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return sum(sorted(l[:mid])) / 2.0 + sorted(l[mid])[0]
    return sorted(l)[mid
