

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) != len(l2):
        raise ValueError("Lists must have the same length")
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)
    result = []
    for i in range(len(sorted_l1)):
        if sorted_l1[i] == sorted_l2[i]:
            result.append(sorted_l1[i])
            for j in range(i, len(sorted_l1)):
                if sorted_l1[j] == sorted_l2[j]:
                    result.append(sorted_l2[j])
                    break
    return result
