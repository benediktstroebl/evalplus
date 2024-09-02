

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # sort both lists
    l1 = sorted(l1)
    l2 = sorted(l2)

    # find the indices of the elements in l2
    indices = [i for i, v in enumerate(l2) if v in l1]

    # get the elements in l1 that appear in l2
    common = [l1[i] for i in indices]

    # remove the elements from l1 that are not in l2
    return [c for c in l1 if c not in common]
