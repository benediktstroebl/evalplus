

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    l_length = len(l)
    if l_length % 2 == 0:
        return (l[l_length // 2] + l[l_length // 2 - 1]) / 2
    else:
        return l[l_length // 2]

