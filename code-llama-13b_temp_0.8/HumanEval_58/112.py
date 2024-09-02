

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # common(l1: list, l2: list)

    # 1.
    # common_set = set(l1).intersection(set(l2))

    # 2.
    # common_set = set()
    # for item in l1:
    #     if item in l2:
    #         common_set.add(item)

    # 3.
    common_set = set(l1).intersection(set(l2))

    # 4.
    # common_set = set(l1).intersection(set(l2))
    # common_list = list(common_set)
    # common_list.sort()

    return sorted(list(common_set))

