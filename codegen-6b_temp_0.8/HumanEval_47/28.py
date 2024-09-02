

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sortedL = sorted(l)
    size = len(sortedL)
    if size % 2:
        return sortedL[size // 2]
    else:
        middle = size // 2
        return (sortedL[middle - 1] + sortedL[middle]) / 2
