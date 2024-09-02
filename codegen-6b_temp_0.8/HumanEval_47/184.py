

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    num_middle = len(l) // 2
    if len(l) % 2:
        # odd case
        return l[num_middle]
    else:
        # even case
        return (l[num_middle - 1] + l[num_middle]) / 2

