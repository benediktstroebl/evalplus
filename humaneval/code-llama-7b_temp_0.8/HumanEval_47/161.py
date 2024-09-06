

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l = sorted(l)
    if len(l) % 2 == 1:
        m = l[int((len(l) - 1) / 2)]
    else:
        m = (l[int(len(l) / 2)] + l[int(len(l) / 2 - 1)]) / 2
    return m

