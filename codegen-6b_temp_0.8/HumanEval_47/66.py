

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    s = sorted(l)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    else:
        median = (s[n // 2 - 1] + s[n // 2]) / 2
        return median
