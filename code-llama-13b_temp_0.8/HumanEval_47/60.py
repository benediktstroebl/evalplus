

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    copy_l = l[:]
    copy_l.sort()
    n = len(copy_l)
    if n % 2 == 1:
        return copy_l[n // 2]
    else:
        return (copy_l[n // 2] + copy_l[n // 2 - 1]) / 2



