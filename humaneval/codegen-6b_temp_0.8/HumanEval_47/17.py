

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    for i in l:
        if i % 2 == 0:
            return i
    if len(l) % 2 == 1:
        return l[-1]
    else:
        return (l[-1] + l[-2]) / 2
