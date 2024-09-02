

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    copy = sorted(l)  # copies the list l
    length = len(copy)
    middle_index = length // 2

    if length % 2 == 1:
        return copy[middle_index]
    else:
        return (copy[middle_index - 1] + copy[middle_index]) / 2

