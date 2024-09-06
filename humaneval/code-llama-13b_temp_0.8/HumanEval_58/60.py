

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # common(l1: list, l2: list)
    # 1. if l1 is larger than l2, swap l1 with l2
    if len(l1) > len(l2):
        l1, l2 = l2, l1
    # 2. create empty list and iterate through l1
    result = []
    for i in l1:
        # if l2 contains i, add it to the result
        if i in l2:
            result.append(i)
    return sorted(set(result))

