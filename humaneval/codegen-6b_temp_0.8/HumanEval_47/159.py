

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list
    l = sorted(l)
    # Find the middle position
    n = len(l)
    mid = n//2
    # If n is odd, return the middle element
    if n % 2 == 1:
        return l[mid]
    # If n is even, return the average of middle 2 elements
    return (l[mid - 1] + l[mid])/2
