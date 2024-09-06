

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) < len(l2):
        l1, l2 = l2, l1
    l1_len = len(l1)
    l2_len = len(l2)
    common = {}
    for i in range(l1_len):
        if l1[i] in common:
            common[l1[i]] += 1
        else:
            common[l1[i]] = 1
        if l1[i] == l2[i]:
            common[l1[i]] -= 1
    common_list = []
    for key, value in common.items():
        if value > 0:
            common_list.append(key)
    common_list.sort()
    return common_list

