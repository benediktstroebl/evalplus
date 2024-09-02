

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    ordered = sorted(l)
    length = len(l)

    if length % 2 == 1:
        return ordered[length // 2]
    else:
        middle_index = length // 2
        return (ordered[middle_index - 1] + ordered[middle_index]) / 2.0

