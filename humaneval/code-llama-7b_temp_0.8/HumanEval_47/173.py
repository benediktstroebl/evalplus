

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)

    # Calculate median
    if len(l) % 2 == 1:
        median_index = len(l) // 2
        return sorted_l[median_index]
    else:
        lower_index = len(l) // 2 - 1
        upper_index = lower_index + 1
        return (sorted_l[lower_index] + sorted_l[upper_index]) / 2

