

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_copy = sorted(l)
    if len(l_copy) % 2 == 0:
        mid_l = l_copy[len(l_copy) // 2]
        mid_r = l_copy[len(l_copy) // 2 - 1]
        return (mid_l + mid_r) / 2
    else:
        return l_copy[len(l_copy) // 2]

