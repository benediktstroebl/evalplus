

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_sorted = sorted(l)
    length = len(l)
    mid_index = length // 2
    if length % 2 == 0:
        median = (l_sorted[mid_index] + l_sorted[mid_index - 1]) / 2
    else:
        median = l_sorted[mid_index]
    return median
