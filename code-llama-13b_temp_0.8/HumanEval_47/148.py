

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    copy_list = sorted(l)
    n = len(copy_list)
    if n % 2:
        return copy_list[n // 2]
    else:
        return (copy_list[n // 2] + copy_list[n // 2 - 1]) / 2

