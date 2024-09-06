

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    half_len = len(l) // 2
    if half_len < 1:
        return 0
    if half_len % 2:
        return l[half_len]
    else:
        return (l[half_len] + l[half_len - 1]) / 2
