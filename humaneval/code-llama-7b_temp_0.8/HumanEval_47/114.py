

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list.
    l.sort()
    # Return the middle element if list has odd number of elements.
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    # Return mean of middle two elements if list has even number of elements.
    return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2

