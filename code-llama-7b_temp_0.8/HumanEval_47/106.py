

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) == 0:
        raise ValueError("median() arg is an empty sequence")

    sorted_list = l.copy()
    sorted_list.sort()

    if len(l) == 1:
        return l[0]
    elif len(l) % 2 == 0:
        mid_high = len(l) // 2
        mid_low = mid_high - 1
        return (sorted_list[mid_low] + sorted_list[mid_high]) / 2
    else:
        mid_high = (len(l) + 1) // 2
        return sorted_list[mid_high - 1]

