

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Write your code here.
    # 1. convert the list to set
    # 2. Convert the set to list
    # 3. Sort the list
    l1_set = set(l1)
    l2_set = set(l2)
    # print(l1_set)
    # print(l2_set)
    l3 = list(l1_set.intersection(l2_set))
    return sorted(l3)

