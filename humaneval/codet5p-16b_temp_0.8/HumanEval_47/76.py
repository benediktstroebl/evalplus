

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    s = sorted(l)
    m = len(s)
    if m % 2 == 0:
        return (s[m//2-1]+s[m//2])/2
    else:
        return s[m//2]
