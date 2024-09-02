

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    # find the middle index
    mid = len(l) / 2
    # if list is even number then is the median
    if len(l) % 2 == 1:
        return l[mid]
    # if list is odd number then is the average of the two median indices
    else:
        return (l[mid-1] + l[mid]) / 2.0
    raise NotImplementedError

