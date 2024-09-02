

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """
    As we are assuming the list to be a sorted list we are using binary search to find the element
    at the middle of the list and return that as the median value
    """
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2] + l[n // 2 - 1]) / 2
    return l[n // 2]
