

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)  # Sort the list, if it isn't already.

    # For even-length list, return mean of middle two elements.
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    # For odd-length list, return middle element.
    else:
        return l[len(l) // 2]
