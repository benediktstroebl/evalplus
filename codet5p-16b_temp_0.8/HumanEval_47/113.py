

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    if len(l) == 0:
        return 0
    sorted_list = sorted(l)
    median = (len(l) - 1) // 2
    if len(l) % 2 == 1:
        return sorted_list[median]
    return (sorted_list[median] + sorted_list[median + 1]) / 2

