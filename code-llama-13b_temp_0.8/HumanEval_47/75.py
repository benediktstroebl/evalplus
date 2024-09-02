

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """
    n = len(l)
    l.sort()
    if n % 2 == 0:
        median1 = l[n//2]
        median2 = l[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = l[n//2]
    return median
    """
    return ((len(l) % 2) == 0 and (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2 or l[len(l) // 2]) if l else None

