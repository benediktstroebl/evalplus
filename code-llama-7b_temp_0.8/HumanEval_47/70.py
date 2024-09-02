

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    s = sorted(l)
    half, odd = divmod(len(s), 2)
    if odd:
        return s[half]
    return (s[half-1] + s[half]) / 2.0
