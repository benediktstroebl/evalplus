

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # 1
    l.sort()
    # 2
    if l[0] < l[-1]:
        # 3
        if len(l) % 2 == 0:
            # 4
            m1 = l[len(l) // 2]
            m2 = l[len(l) // 2 - 1]
            return (m1 + m2) / 2
        # 5
        else:
            return l[len(l) // 2]
    # 6
    else:
        return -1

