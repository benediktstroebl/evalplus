

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    length = len(sorted_l)
    if length % 2 == 0:
        mid1 = length // 2 - 1
        mid2 = mid1 + 1
        return (sorted_l[mid1] + sorted_l[mid2]) / 2
    else:
        mid = length // 2
        return sorted_l[mid]
