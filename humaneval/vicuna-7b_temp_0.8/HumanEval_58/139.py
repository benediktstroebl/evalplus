

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    n1 = len(l1)
    n2 = len(l2)
    m = max(n1, n2)
    r = [[set(l1[i:i+1]) & set(l2[i:i+1]) for i in range(0, n1, 1)] for _ in range(m)]
    return [sorted(x)[0] for x in r]