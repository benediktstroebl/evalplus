

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    n1 = len(l1)
    n2 = len(l2)
    m = n1 if n1 >= n2 else n2
    if m == 0:
        return []

    a = sorted(l1)
    b = sorted(l2)
    a_idx = 0
    b_idx = 0

    for i in range(m):
        if a[a_idx] == b[b_idx]:
            a_idx += 1
            b_idx += 1
        else:
            yield a[a_idx], b[b_idx]
            a_idx += 1
            b_idx = 0 if b_idx == n2 else 1
    yield a[a_idx], b[b_idx]
