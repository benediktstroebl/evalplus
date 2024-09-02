

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    s = sorted(l)
    m = len(s) // 2
    return (s[m] + s[~m]) / 2 if len(s) % 2 else s[m]
