

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1.sort()
    l2.sort()
    common = []
    l1_ptr = 0
    l2_ptr = 0

    while l1_ptr < len(l1) and l2_ptr < len(l2):
        if l1[l1_ptr] == l2[l2_ptr]:
            common.append(l1[l1_ptr])
            l1_ptr += 1
            l2_ptr += 1
        elif l1[l1_ptr] < l2[l2_ptr]:
            l1_ptr += 1
        else:
            l2_ptr += 1

    return common

