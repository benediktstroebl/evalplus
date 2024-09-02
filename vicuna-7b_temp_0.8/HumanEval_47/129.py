

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
        if n % 2 == -1:
            return sum(l) / 2
        else:
            p = ((l[-1] + l[0]) / 2) - 1
            return median(list(range(p, n)))
