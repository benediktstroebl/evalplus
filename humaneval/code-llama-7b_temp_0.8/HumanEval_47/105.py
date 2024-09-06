

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    assert len(l) != 0, "median is not defined for an empty list"
    sorted_list = sorted(l)
    half = len(sorted_list) // 2
    return (sorted_list[half] + sorted_list[~half]) / 2.0 if len(sorted_list) % 2 else float(sorted_list[half])


