

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    n = len(l)
    if n == 0:
        return None
    else:
        i = n // 2
        if n % 2 == 1:
            return l[i]
        else:
            return (l[i - 1] + l[i]) /
