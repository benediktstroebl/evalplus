

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    assert len(l1) > 0, "List 1 must have at least one item"
    assert len(l2) > 0, "List 2 must have at least one item"
    c1 = l1[0]
    c2 = l2[0]
    if c1 == c2:
        return [c1] + common(l1[1:], l2[1:])
    else:
        return [c1, c2] + common(l1[1:], l2[1:])

