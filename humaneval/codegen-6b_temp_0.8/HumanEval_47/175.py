

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_lst = sorted(l)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2.0
    else:
        return sorted_lst[length // 2]

