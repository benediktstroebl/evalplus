

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1_dict = {}
    for x in l1:
        l1_dict[x] = 1

    l2_dict = {}
    for x in l2:
        l2_dict[x] = 1

    l1_unique = set(l1_dict)
    l2_unique = set(l2_dict)

    l1_in_l2 = list(l1_unique & l2_unique)

    return sorted(l1_in_l2)

