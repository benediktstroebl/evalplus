

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # # Solution 1: Using sort()
    # l1.sort()
    # l2.sort()
    # lc = []
    # for num in l1:
    #     if num in l2:
    #         lc.append(num)
    #         l2.remove(num)
    # return sorted(lc)

    # Solution 2: Using a set
    l1_set = set(l1)
    l2_set = set(l2)
    lc = l1_set.intersection(l2_set)
    return sorted(lc)
