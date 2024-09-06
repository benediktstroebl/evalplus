

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sort = sorted(l)
    if len(l) % 2 == 0:
        return (sort[int(len(l)/2)] + sort[int(len(l)/2 - 1)])/2
    else:
        return sort[int(len(l)/2)]
