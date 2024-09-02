

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    is_even = len(l) % 2 == 0
    if is_even:
        return float(sum(sorted(l)[int(len(l)/2)-1:int(len(l)/2)+1]) / 2)
    else:
        return float(sorted(l)[int(len(l)/2)])
