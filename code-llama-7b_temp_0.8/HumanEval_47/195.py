

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    s_l = sorted(l)
    size = len(l)
    if size % 2 == 1:
        return s_l[size // 2]
    else:
        return (s_l[size // 2] + s_l[size // 2 - 1]) / 2.0

