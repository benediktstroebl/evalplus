

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    size = len(l)
    middle = (size - 1) // 2
    if size % 2 == 1:  # odd
        return l[middle]
    else:
        return (l[middle] + l[middle+1]) / 2.0

