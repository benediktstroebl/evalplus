

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    n1, n2 = len(l1), len(l2)
    d = {}
    for i in range(n1):
        d[l1[i]] = i
    for i in range(n2):
        d[l2[i]] = i
    for k in d.keys():
        d[k] += 1
    for k in list(d.keys()):
        if d[k] > 1:
            yield k

    for i in range(n1, n1 + min(n2, len(l1))):
        if l1[i] in d:
            yield l1[i]