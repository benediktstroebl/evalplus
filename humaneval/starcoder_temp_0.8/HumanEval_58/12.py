

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    common_list = []
    l1_len = len(l1)
    l2_len = len(l2)
    l1_index = 0
    l2_index = 0

    while l1_index < l1_len and l2_index < l2_len:
        if l1[l1_index] == l2[l2_index]:
            common_list.append(l1[l1_index])
            l1_index += 1
            l2_index += 1
        elif l1[l1_index] < l2[l2_index]:
            l1_index += 1
        else:
            l2_index += 1
    return common_list
