

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    len = len(l)
    if len % 2 == 0:
        median = (l[len // 2 - 1] + l[len // 2]) / 2
    else:
        median = l[len // 2]
    return median

