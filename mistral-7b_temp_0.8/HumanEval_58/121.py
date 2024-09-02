

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # l1.sort()
    # l2.sort()
    # sorted_l1 = list(sorted(l1))
    # sorted_l2 = list(sorted(l2))
    # result = []

    # for i in range(len(sorted_l1)):
    #     if sorted_l1[i] in sorted_l2:
    #         result.append(sorted_l1[i])

    # return result
    return sorted(set(l1) & set(l2))




