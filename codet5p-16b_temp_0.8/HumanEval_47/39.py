

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    sorted_l = sorted(l)
    mid_index = int(len(l)/2)
    mid_val = sorted_l[mid_index]
    if len(l) % 2!= 0:
        return mid_val
    return (mid_val + sorted_l[mid_index - 1]) / 2.0
