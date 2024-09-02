

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1_freq = {}
    l2_freq = {}
    common = []

    for elem in l1:
        l1_freq[elem] = l1_freq.get(elem, 0) + 1

    for elem in l2:
        l2_freq[elem] = l2_freq.get(elem, 0) + 1

    for elem, freq in l1_freq.items():
        if elem in l2_freq:
            common.append(elem)

    return sorted(common)

