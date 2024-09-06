

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        mid = n // 2
        return (median(l[mid:mid+1]) + median(l[:mid])) / 2.0
    else:
        return (median(l[0:mid]) + median(l[mid+1:])) / 2.0
