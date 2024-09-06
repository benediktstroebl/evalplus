

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    l_len = len(l)

    if not l_len:
        raise ValueError('Cannot compute median of empty list')

    if l_len == 1:
        return l[0]

    if l_len % 2:
        return l[l_len//2]

    return (l[l_len//2] + l[(l_len//2 - 1)]) / 2

