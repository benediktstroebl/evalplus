

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # l1.sort()
    # l2.sort()
    # for i in range(len(l1) - 1):
    #     if l1[i] != l1[i + 1]:
    #         l1.insert(i + 1, l1[i + 1])
    # for i in range(len(l2) - 1):
    #     if l2[i] != l2[i + 1]:
    #         l2.insert(i + 1, l2[i + 1])
    # l1 = sorted(l1)
    # l2 = sorted(l2)
    # c = []
    # i = 0
    # j = 0
    # while i < len(l1) and j < len(l2):
    #     if l1[i] == l2[j]:
    #         c.append(l1[i])
    #         i += 1
    #         j += 1
    #     elif l1[i] < l2[j]:
    #
