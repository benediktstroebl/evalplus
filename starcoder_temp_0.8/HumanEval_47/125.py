

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort
    l.sort()
    # if even
    if len(l) % 2 == 0:
        m1, m2 = l[len(l)//2], l[len(l)//2-1]
        return (m1+m2)/2
    # if odd
    else:
        m = l[len(l)//2]
        return m
