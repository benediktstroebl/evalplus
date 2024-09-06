

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list l.
    l.sort()
    # Calculate the median of the list l.
    if len(l) % 2 == 1:
        median = l[len(l) // 2]
    else:
        median = (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    return median

