

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sort = insertion_sort(l)
    mid = len(sort) // 2
    if len(sort) % 2:
        return sort[mid]
    else:
        return (sort[mid - 1] + sort[mid]) / 2
