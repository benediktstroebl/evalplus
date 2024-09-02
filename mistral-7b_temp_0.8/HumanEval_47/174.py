

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Start by sorting the list.
    l.sort()

    # The median value is the middle value in a list with an odd length.
    # For a list with an even length, the median is the average of the
    # two middle values.
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2

