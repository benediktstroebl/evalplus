

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    length = len(l)
    if length == 0:
        raise ValueError("Can't find median of empty list.")
    elif length == 1:
        return l[0]
    elif length % 2 == 0:
        return (l[length // 2 - 1] + l[length // 2]) / 2.0
    else:
        return l[length // 2]

