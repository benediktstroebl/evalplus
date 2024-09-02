

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    len_l = len(l)
    if len_l % 2 == 1:
        return l[len_l // 2]
    else:
        return (l[len_l // 2 - 1] + l[len_l // 2]) /
