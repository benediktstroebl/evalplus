

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    assert(len(l) > 0)
    mid = (len(l) + 1) // 2
    left = l[:mid]
    right = l[mid:]
    if len(left) == 0:
        return l[mid]
    if len(left) % 2 == 1:
        return left[mid // 2]
    else:
        return (left[mid // 2] + left[(mid // 2) - 1]) / 2.0

