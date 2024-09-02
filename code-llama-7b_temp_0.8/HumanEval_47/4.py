

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)

    if len(l) == 0:
        raise ValueError("median() arg is an empty sequence")

    median_index = (len(l) - 1) // 2
    if (len(l) % 2) == 0:
        return (l[median_index] + l[median_index + 1]) / 2
    return l[median_index]

