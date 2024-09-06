

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        return None
    # l is an odd number of elements
    if len(l) % 2 == 1:
        return l[(len(l) - 1) // 2]
    # l is an even number of elements
    else:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2

