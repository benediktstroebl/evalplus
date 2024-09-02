

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    copy_list = sorted(l)
    if len(copy_list) % 2 == 1:
        middle = len(copy_list) // 2
        return copy_list[middle]
    else:
        middle1 = len(copy_list) / 2 - 1
        middle2 = len(copy_list) / 2
        return (copy_list[middle1] + copy_list[middle2]) / 2.0

