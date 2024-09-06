

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    copy_l = l.copy()
    copy_l.sort()
    length = len(copy_l)
    if length % 2 == 0:
        return (copy_l[length // 2 - 1] + copy_l[length // 2]) / 2
    else:
        return copy_l[length // 2]

