

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) == 0:
        return None
    else:
        # lst_sorted = sorted(l)
        lst_sorted = sorted(l, reverse=True)
        return lst_sorted[len(l) // 2]


