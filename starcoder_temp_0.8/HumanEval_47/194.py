

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    index = len(l) // 2
    if len(l) % 2:
        return sorted_l[index]
    else:
        return (sorted_l[index-1] + sorted_l[index]) / 2

