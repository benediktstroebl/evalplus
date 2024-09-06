

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        return sum(l) / 2
    else:
        l[0] = l[0] if l[0] < 0 else 0
        return sum(l[1:]) / 2