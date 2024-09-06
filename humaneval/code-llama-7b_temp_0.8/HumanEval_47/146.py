

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # working with odd number of elements
    if len(l) % 2 != 0:
        return l[len(l)//2]

    # working with even number of elements
    l1 = l[:len(l)//2]
    l2 = l[len(l)//2:]
    return sum(l1) / 2 if l1 == l2 else (sum(l1) + sum(l2)) / 2

