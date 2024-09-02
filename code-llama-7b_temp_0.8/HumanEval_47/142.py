

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the elements of l in place
    l.sort()
    # Get the size of the list
    sz = len(l)
    # If the size is odd, return the middle element
    if sz % 2 == 1:
        return l[sz // 2]
    # If the size is even, get the average of the two middle elements
    else:
        middle_low = sz // 2
        middle_high = middle_low - 1
        return (l[middle_low] + l[middle_high]) / 2

