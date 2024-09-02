

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sortl = sorted(l)
    n = len(l)
    return sortl[n//2] if n % 2 else (sortl[n//2] + sortl[n//2 - 1])/2
