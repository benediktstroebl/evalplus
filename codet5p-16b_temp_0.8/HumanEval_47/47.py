

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    if len(l) == 0:
        raise ValueError('Empty list')
    s = sorted(l)
    n = len(l)
    if n % 2 == 1:
        return float(s[n // 2])
    else:
        return float(0.5 * (s[n // 2 - 1] + s[n // 2]))
