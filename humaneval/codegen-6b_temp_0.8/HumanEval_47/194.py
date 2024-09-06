

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l) # try using l.sort()
    n = len(sorted_l)
    if n == 0:
        raise ValueError("median of empty list")
    elif n % 2 == 1:
        return sorted_l[(n - 1) // 2]
    else:
        return sorted_l[(n - 1) // 2]
