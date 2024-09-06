

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Raise an Exception if l is empty.
    if len(l) == 0:
        raise ValueError("Empty list")

    # Sort the elements.
    l.sort()

    # Return the median.
    return l[len(l) // 2]

