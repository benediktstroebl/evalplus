

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # You may want to use the sort method.
    # For example, l.sort() sorts l in place.
    l.sort()
    size = len(l)
    if size % 2 == 1:
        return l[int((size - 1) / 2)]
    else:
        return (l[int(size / 2)] + l[int(size / 2 - 1)]) / 2

