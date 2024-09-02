

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    sorted_list = sorted(l)
    n = len(sorted_list)
    median = 0.0

    if n % 2 == 1:
        median = sorted_list[(n - 1) // 2]
    else:
        median = (sorted_list[n // 2] + sorted_list[n // 2 - 1]) / 2.0

    return median

