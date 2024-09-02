

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        # even
        median_index = length // 2
        median = (l[median_index - 1] + l[median_index]) / 2
        return median
    else:
        # odd
        median_index = length // 2
        median = l[median_index]
        return median

