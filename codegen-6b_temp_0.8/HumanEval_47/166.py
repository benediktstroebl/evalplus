

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) == 0:
        return 0
    l.sort()
    mid_index = int(len(l) / 2)
    if len(l) % 2 == 0:
        return (l[mid_index] + l[mid_index - 1]) / 2
    return l[mid_index]

