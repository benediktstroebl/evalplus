

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    length = len(l)
    if length % 2 == 0:
        median = (l[int(length/2)] + l[int(length/2-1)]) / 2
    else:
        median = l[int((length-1)/2)]

    return median

