

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    index = (len(l) - 1) // 2
    if len(l) % 2:
        return l[index]
    else:
        return (l[index] + l[index + 1]) / 2.0
