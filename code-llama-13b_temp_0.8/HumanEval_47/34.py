

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    copy_list = sorted(l)
    if len(copy_list) % 2 == 1:
        return copy_list[int((len(copy_list) + 1) / 2) - 1]
    else:
        return (copy_list[int(len(copy_list) / 2)] + copy_list[int(len(copy_list) / 2 - 1)]) / 2.0

