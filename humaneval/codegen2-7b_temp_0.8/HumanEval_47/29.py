

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n == 0:
        return 0
    if n == 1:
        return l[0]
    l.sort()
    return l[n//2]
