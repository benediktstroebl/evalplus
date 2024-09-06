

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    n = len(l)
    # Check if the list has an even number of items
    if n % 2 == 0:
        # If so, return the average of the two middle items
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        # Otherwise, return the middle item
        return l[n//2]
