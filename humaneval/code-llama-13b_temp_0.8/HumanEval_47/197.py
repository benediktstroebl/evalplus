

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    new_list = l[:]
    new_list.sort()
    length = len(new_list)
    if length % 2 == 0:
        return (new_list[length // 2] + new_list[(length // 2) - 1]) / 2
    else:
        return new_list[length // 2]

