

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    sorted_l = sorted(l)
    if len(sorted_l) % 2 == 0:
        mid = (len(sorted_l) // 2)
        median = (sorted_l[mid] + sorted_l[mid - 1]) / 2
        return median
    else:
        mid = (len(sorted_l) // 2)
        median = sorted_l[mid]
        return median
        
        
        
