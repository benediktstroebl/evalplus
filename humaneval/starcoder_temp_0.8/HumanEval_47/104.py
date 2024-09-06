

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sort_l = sorted(l)
    return (sort_l[len(l)//2] + sort_l[~len(l)//2]) / 2
