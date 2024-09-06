

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if isinstance(l1, list):
        l1 = l1.copy()
    if isinstance(l2, list):
        l2 = l2.copy()

    if len(l1) == 0 or len(l2) == 0:
        return []
    else:
        to_remove = []
        for i in l1:
            if i in l2:
                to_remove.append(i)
        for i in to_remove:
            l1.remove(i)
            l2.remove(i)
        l1.sort()
        l2.sort()
        return l1 + l2
