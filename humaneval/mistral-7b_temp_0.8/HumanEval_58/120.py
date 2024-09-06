

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    common = []
    # print(l1)
    # print(l2)
    # print(l1[0])
    # print(l2[0])
    # print(type(l1[0]))
    # print(type(l2[0]))
    # print(l1[0] == l2[0])
    # print(l1[0] in l2)
    # print(l1[0] in l2[0])
    # print(l1[0] is l2[0])

    for i in l1:
        # print(i in l2)
        if i in l2:
            # print(i)
            # print(l2)
            # print(l2[0] == i)
            # print(i == l2[0])
            if i not in common:
                common.append(i)
    return sorted(common)

