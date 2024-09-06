

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    s = list(l)
    s.sort()
    mid = int(len(s) / 2)
    return (s[mid] + s[~mid]) / 2 if len(s) % 2 == 0 else s[mid]

