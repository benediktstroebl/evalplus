

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()

    if not l:
        return None
    elif (len(l) % 2) == 0:
        n = int(len(l) / 2)
        return 0.5 * (l[n - 1] + l[n])
    else:
        return l[int(len(l) / 2)]

