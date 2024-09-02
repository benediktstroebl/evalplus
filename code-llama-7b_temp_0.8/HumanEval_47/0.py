

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)
    # calculate median
    if n % 2 == 0:
        median_val = (sorted_list[(n//2)] + sorted_list[(n//2)-1]) / 2
    else:
        median_val = sorted_list[n//2]
    return median_val

