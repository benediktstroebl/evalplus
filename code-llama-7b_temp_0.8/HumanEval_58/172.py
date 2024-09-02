

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # l1 = list(set(l1))
    # l2 = list(set(l2))
    # unique = lambda l: [i for n, i in enumerate(l) if i not in l[:n]]
    # inter = lambda l1, l2: unique(list(set(l1).intersection(set(l2))))
    # return sorted(inter(l1, l2))

    # l1 = list(set(l1))
    # l2 = list(set(l2))
    # c = [i for i in l1 if i in l2]
    # return sorted(c)

    l1 = list(set(l1))
    l2 = list(set(l2))
    return sorted(set(l1) & set(l2))

