

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    length = len(l)
    half_length = int(length / 2)
    if length % 2 == 0:
        median_ = l[half_length - 1] + l[half_length]
        return median_ / 2
    else:
        return l[half_length]

