

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    len = len(l)
    midpoint = len // 2
    if len % 2 == 0:
        return (l[midpoint - 1] + l[midpoint]) / 2
    else:
        return l[midpoint]
