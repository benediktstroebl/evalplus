

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    l_len = len(sorted_l)
    if l_len % 2 == 1:
        return sorted_l[l_len // 2]
    else:
        return (sorted_l[l_len // 2] + sorted_l[l_len // 2 - 1]) / 2

