

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # l1 = l
    # l1.sort()
    # return l1[len(l1)//2]
    print("l", l)
    l1 = sorted(l)
    print("sorted l1", l1)
    if len(l1) % 2 == 0:
        return (l1[len(l1)//2] + l1[len(l1)//2-1]) / 2
    else:
        return l1[len(l1)//2]

