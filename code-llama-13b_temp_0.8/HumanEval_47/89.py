

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    l.sort()
    mid_index = n // 2
    if n % 2 == 0:
        median_value = (l[mid_index] + l[mid_index - 1]) / 2
    else:
        median_value = l[mid_index]
    return median_value
