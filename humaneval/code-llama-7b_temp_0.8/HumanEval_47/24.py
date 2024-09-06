

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list if it isn't sorted.
    l = sorted(l)
    # Even length.
    if len(l) % 2 == 0:
        mid = int(len(l) / 2)
        return (l[mid] + l[mid - 1]) / 2
    # Odd length.
    else:
        mid = int(len(l) / 2)
        return l[mid]

