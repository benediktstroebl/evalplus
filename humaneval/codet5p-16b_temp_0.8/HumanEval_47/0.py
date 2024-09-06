

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    n = len(l)
    if n % 2 == 1:
        return sorted(l)[n//2]
    else:
        return sum(sorted(l)[n//2-1:n//2+1])/2.0
