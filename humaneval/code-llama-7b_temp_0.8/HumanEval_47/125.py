

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # Sort the list
    l = sorted(l)

    # Find the center index
    index = len(l) // 2

    # If odd, return center element. If even, return average of center elements
    if len(l) % 2 == 0:
        return (l[index - 1] + l[index]) / 2.0
    else:
        return l[index]
