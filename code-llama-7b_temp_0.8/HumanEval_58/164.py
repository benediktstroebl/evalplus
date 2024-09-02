

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1_counts = {l1[i]: 1 for i in range(len(l1))}
    l2_counts = {l2[j]: 1 for j in range(len(l2))}

    common_counts = {x: l1_counts[x] + l2_counts[x]
                     for x in l1_counts if x in l2_counts}

    return sorted(set(common_counts))

