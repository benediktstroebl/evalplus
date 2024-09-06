

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # The number of items in the list
    n = len(l)
    # The middle index
    i = n // 2
    # Base case: For an odd list, the median is the middle element
    if n % 2 == 1:
        return l[i]
    # For an even list, the median is the average of the two middle elements
    else:
        return (l[i - 1] + l[i]) / 2
