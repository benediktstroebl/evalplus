

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    copy = l.copy()
    copy.sort()

    if len(copy) % 2 == 0:
        return (copy[len(copy) // 2] + copy[len(copy) // 2 - 1]) / 2
    else:
        return copy[len(copy) // 2]

