

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Correction for edge case.
    if len(l1) > len(l2):
        l1, l2 = l2, l1

    # We will set the key to the element value.
    l1 = list(enumerate(l1))
    l2 = list(enumerate(l2))
    l2.sort(key=lambda x: x[1])
    l2 = [x[0] for x in l2]

    # Start at the end of the first list as we are appending to it.
    i1, i2 = len(l2) - 1, len(l1) - 1
    idx, idx2 = 0, 0

    while i1 >= 0 and i2 >= 0:
        if l1[i1][1] == l2[i2]:
            yield l1[i1][1]
            idx += 1
            i1 -= 1
            i2 -= 1
        elif l1[i1][1] > l2[i2]:
            i2 -= 1
        else:
            i1 -= 1

    return

