

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    copy = l.copy()
    copy.sort()

    if len(copy) % 2 == 1:
        return copy[int(len(copy)/2)]
    else:
        return (copy[int(len(copy)/2)] + copy[int(len(copy)/2) - 1]) / 2

