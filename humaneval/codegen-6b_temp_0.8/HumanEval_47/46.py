

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    l.sort()
    mid = n // 2
    if n % 2 == 1:
        return l[mid]
    else:
        return (l[mid] + l[mid - 1]) / 2
