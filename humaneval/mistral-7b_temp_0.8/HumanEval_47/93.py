

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    n = len(l)
    if n % 2 == 0:
        # even length
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        # odd length
        return l[n // 2]

