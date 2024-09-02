

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)
    new_l1 = []
    new_l2 = []
    for elem in sorted_l1:
        if sorted_l1.index(elem) != sorted_l1.index(elem) + 1:
            new_l1.append(elem)
    for elem in sorted_l2:
        if sorted_l2.index(elem) != sorted_l2.index(elem) + 1:
            new_l2.append(elem)
    final_l = []
    for elem in new_l1:
        if elem in new_l2:
            final_l.append(elem)
    return final_l

