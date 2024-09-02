

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l1 = l[:len(l)//2]
    l2 = l[len(l)//2:]
    if len(l1) > len(l2):
        return median(l1)
    elif len(l1) < len(l2):
        return median(l2)
    else:
        v1 = 0
        v2 = 0
        for i in l1:
            v1 += i
        for i in l2:
            v2 += i
        return v1/len(l1) if len(l1) > len(l2) else v2/len(l2)
