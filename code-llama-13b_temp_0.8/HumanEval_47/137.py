

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_len = len(l)
    l_sorted = sorted(l)
    if l_len % 2 == 0:
        return (l_sorted[int(l_len / 2) - 1] + l_sorted[int(l_len / 2)]) / 2
    return l_sorted[int(l_len / 2)]

