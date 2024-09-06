

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    lst = sorted(l)
    r = len(lst)
    if r == 0:
        return None
    if r % 2 == 1:
        return lst[int((r-1)/2)]
    else:
        return float(lst[int((r-1)/2)] + lst[int((r-1)/2)+1])/2

