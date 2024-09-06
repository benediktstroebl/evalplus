

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    midpoint = len(sorted_l) // 2

    if len(sorted_l) % 2:
        return sorted_l[midpoint]
    else:
        return (sorted_l[midpoint] + sorted_l[midpoint - 1]) / 2
