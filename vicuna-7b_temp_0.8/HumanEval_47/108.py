

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort the list
    l = sorted(l)
    # determine the middle index
    n = len(l)
    if n % 2 == 0:
        # even number of elements
        return (n // 2) + 1
    else:
        # odd number of elements
        return (n // 2) + 2
