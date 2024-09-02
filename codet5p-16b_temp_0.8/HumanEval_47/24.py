

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    if len(l) == 0:
        return None
    sorted_list = sorted(l)
    median_index = len(l) // 2
    if len(l) % 2 == 1:
        return sorted_list[median_index]
    else:
        return (sorted_list[median_index] + sorted_list[median_index - 1]) / 2
