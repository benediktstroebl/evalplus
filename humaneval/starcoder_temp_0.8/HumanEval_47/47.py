

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # 1. Sort the list
    l.sort()
    # 2. Find the mid point
    mid = len(l) // 2
    # 3. Return the element at the mid point
    return l[mid]
