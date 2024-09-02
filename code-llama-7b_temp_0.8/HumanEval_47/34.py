

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    # Middle element of list
    mid = len(l) // 2

    # If list length is odd, return middle element
    if len(l) % 2 != 0:
        return sorted_list[mid]
    # If list length is even, return average of middle two elements
    else:
        return (sorted_list[mid] + sorted_list[mid - 1]) / 2

