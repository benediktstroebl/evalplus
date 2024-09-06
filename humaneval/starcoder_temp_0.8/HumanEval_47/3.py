

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    size = len(l)
    if size % 2 == 1:
        return sorted(l)[size//2]
    else:
        first = sorted(l)[size//2-1]
        second = sorted(l)[size//2]
        return (first+second)/2
