

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    num = len(l)
    result = 0.0
    if num % 2 == 0:
        result = (l[num // 2 - 1] + l[num // 2]) / 2
    else:
        result = l[num // 2]
    return result

