

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) % 2 == 0:
        mid = int(len(l)/2)
        return (l[mid] + l[mid-1])/2
    else:
        return l[(len(l) - 1) // 2]
