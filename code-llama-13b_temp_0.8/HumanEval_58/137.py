

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # 3.14
    # def common_elements(l1, l2):
    #     return list(set(l1) & set(l2))
    # print(common_elements([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
    # print(common_elements([5, 3, 2, 8], [3, 2]))

    # 3.13
    # def common_elements(l1, l2):
    #     common = []
    #     for e1 in l1:
    #         for e2 in l2:
    #             if e1 == e2:
    #                 common.append(e1)
    #                 break
    #     return common
    # print(common_elements([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
    # print(common_elements([5, 3, 2, 8], [3, 2]))

    # 3.12
    # def common_elements(l1, l2):
    #     common = []
    #     for e1 in l1:
    #         for e2 in l2:
    #             if e1 == e2:
    #                 common.append(e1)
    #                 break
    #     return common
    # print(common_elements([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
    # print(common_elements([5, 3, 2, 8], [3, 2]))

    # 3.11
    # def common_elements(l1, l2):
    #     common = []
    #     for e1 in l1:
    #         if e1 in l2 and e
