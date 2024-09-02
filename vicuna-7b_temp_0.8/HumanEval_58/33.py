

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    n1 = len(l1)
    n2 = len(l2)

    for i in range(n1):
        for j in range(n2):
            if l1[i] == l2[j]:
                yield l1[i]
                l1.remove(l1[i])
                break
            elif l1[i] < l2[j]:
                break
    for i in range(n1, n1 - len(l2)):
        yield l1[i]
