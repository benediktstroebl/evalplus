

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    length = len(l)
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_l[mid_index - 1] + sorted_l[mid_index]) / 2
    else:
        return sorted_l[mid_index]

