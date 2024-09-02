

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort l;
    l.sort()
    # In case the list has no even number of elements, median() will choose the lower of the two middle elements.
    # In that case, we will use the floor of the middle instead.
    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle - 1] + l[middle]) / 2.0
    else:
        return l[middle]

