

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    n1 = len(l1)
    n2 = len(l2)
    if n1 == 1 and len(l2) == 1:
        if l1[0] == l2[0]:
            return [l1[0]]
        else:
            return []
    elif n2 == 1:
        if l1[0] == l2[0]:
            return [l1[0]]
        else:
            return []
    else:
        for x in l1:
            if x not in l2:
                l2.remove(x)
        return sorted(l2)
