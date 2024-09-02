

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)

    if len(sorted_l) % 2 == 1:
        return sorted_l[(len(sorted_l) - 1) // 2]
    else:
        left = sorted_l[(len(sorted_l) // 2) - 1]
        right = sorted_l[len(sorted_l) // 2]
        return (left + right) / 2

