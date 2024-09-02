

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    # l is sorted now.
    if len(l) % 2 == 0:
        # when length is even
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        # when length is odd
        return l[len(l) // 2]

