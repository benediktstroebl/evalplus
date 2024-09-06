

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("empty list")
    n = len(l)
    l.sort()
    if n % 2 == 1:
        return l[n//2]
    else:
        return (l[n//2]+l[n//2-
