

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    s = sorted(l)
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        return (s[len(s) // 2] + s[(len(s) // 2) - 1]) / 2.0
