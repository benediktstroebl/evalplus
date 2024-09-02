

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = l1 if l1 and not l1 == [] else None
    l2 = l2 if l2 and not l2 == [] else None

    if l1 and l2:
        return sorted(set(l1).intersection(l2))
    elif l1:
        return l1
    elif l2:
        return l2

