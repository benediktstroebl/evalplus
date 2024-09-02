

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    middle = len(sorted_l) // 2
    if len(sorted_l) % 2 == 0:
        return (sorted_l[middle] + sorted_l[middle - 1]) / 2
    else:
        return sorted_l[middle]

