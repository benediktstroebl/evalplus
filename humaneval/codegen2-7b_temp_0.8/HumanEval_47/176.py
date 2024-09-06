

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("Can't calculate the median of an empty list")
    if len(l) == 1:
        return l[0]
    l.sort()
    return (l[len(l)/2] + l[len(l)/2 - 1])/
