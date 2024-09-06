

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_copy = sorted(l)
    n = len(l_copy)
    if n % 2 == 1:
        return l_copy[n // 2]
    else:
        return (l_copy[n // 2 - 1] + l_copy[n // 2]) / 2
