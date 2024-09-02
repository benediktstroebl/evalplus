

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # if the list has length 1, return that element
    if len(l) == 1:
        return l[0]
    # if the list has length 2, return average
    elif len(l) == 2:
        return (l[0] + l[1]) / 2
    # if the list has an odd length, return the middle element
    elif len(l) % 2 == 1:
        return l[int(len(l) / 2)]
    # if the list has an even length, return average of middle two elements
    else:
        return (l[int(len(l) / 2)] + l[int(len(l) / 2) - 1]) / 2

