

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # your code here
    if len(l1) > len(l2):
        l1, l2 = l2, l1

    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                l1.pop(i)

    return l1

