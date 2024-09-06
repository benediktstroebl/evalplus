

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    l_len = len(l)
    return l[l_len//2] if l_len % 2 == 1 else (l[l_len//2] + l[l_len//2 - 1])/2

