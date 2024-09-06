

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        l1 = l[len(l) // 2 - 1]
        l2 = l[len(l) // 2]
        return (l1 + l2) / 2
