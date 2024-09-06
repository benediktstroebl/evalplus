

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sort = l.sort()
    size = len(l)
    index = size // 2
    if size % 2 == 0:
        return (sort[index] + sort[index + 1]) / 2
    else:
        return sort[index]
