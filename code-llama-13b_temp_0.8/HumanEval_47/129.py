

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_sorted = sorted(l)
    length = len(l_sorted)
    if length % 2 == 1:
        return l_sorted[(length - 1) // 2]
    elif length % 2 == 0:
        return (l_sorted[length // 2] + l_sorted[(length - 1) // 2]) / 2

