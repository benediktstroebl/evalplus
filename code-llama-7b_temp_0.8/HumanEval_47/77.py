

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError('Empty list')
    l = sorted(l)  # Makes a copy of the list
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        i = n // 2
        return (l[i - 1] + l[i]) / 2
