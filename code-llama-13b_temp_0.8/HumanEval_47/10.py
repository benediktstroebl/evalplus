

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    copy = sorted(l)
    n = len(copy)
    if n % 2 == 0:
        return (copy[n//2-1] + copy[n//2])/2
    else:
        return copy[n//2]

