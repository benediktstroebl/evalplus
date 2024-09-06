

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # def common_recursive(l1: list, l2: list, l3: list = []):
    #     """Return sorted unique common elements for two lists.
    #     >>> common_recursive([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    #     [1, 5, 653]
    #     >>> common_recursive([5, 3, 2, 8], [3, 2])
    #     [2, 3]

    #     """
    #     if l1:
    #         for i in l1:
    #             if i in l2:
    #                 l3.append(i)
    #                 l2.remove(i)
    #         common_recursive(l1, l2, l3)
    #     else:
    #         return l3
    # return common_recursive(l1, l2
