

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # compute the median.
    if len(l) == 0:
        raise RuntimeError("Empty list")
    l = sorted(l)
    median = None
    if len(l) % 2 == 1:
        median = l[int(len(l) / 2)]
    else:
        median = (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)]) / 2.0
    return median

