

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1.sort()
    l2.sort()
    common_elements = []
    l1_index = 0
    l2_index = 0
    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] == l2[l2_index]:
            common_elements.append(l1[l1_index])
            l1_index += 1
            l2_index += 1
        elif l1[l1_index] > l2[l2_index]:
            l2_index += 1
        else:
            l1_index += 1
    return common_elements
