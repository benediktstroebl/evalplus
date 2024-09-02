

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort the list
    l.sort()
    # divide array in two parts
    if len(l) % 2 == 0:
        # even
        m1 = median(l[:len(l)//2])
        m2 = median(l[len(l)//2:])
        return (m1 + m2) / 2.0
    else:
        # odd
        return l[len(l)//2]

