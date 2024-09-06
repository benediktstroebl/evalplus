

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    k = len(l)
    if k % 2 == 0:
        return (l[k//2] + l[(k//2) - 1]) * 1.0 / 2
    else:
        return l[k//2]
