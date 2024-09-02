

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    s = sorted(l)
    length = len(s)
    if length % 2 == 0:
        return (s[length/2-1] + s[length/2])/2.0
    else:
        return s[length/2
