

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    length = len(l)
    middle = length // 2
    if length % 2 == 0:
        return (l[middle - 1] + l[middle]) / 2
    else:
        return l[middle]

