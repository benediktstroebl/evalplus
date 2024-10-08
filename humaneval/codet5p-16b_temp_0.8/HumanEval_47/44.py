

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    s = sorted(l)
    return s[len(l) // 2] if len(l) % 2 == 1 else 0.5 * (s[len(s) // 2 - 1] + s[len(s) // 2])
