

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    s = l[0]
    for p in l[1:]:
        if s < p:
            s += p
        elif p < s:
            s -= p
    return s / len(l)
