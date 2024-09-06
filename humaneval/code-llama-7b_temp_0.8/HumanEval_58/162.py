

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # Sort the lists and iterate through them, until one is finished.
    l1.sort()
    l2.sort()
    i1, i2 = 0, 0
    output = []
    while i1 < len(l1) and i2 < len(l2):
        # If current elements are equal, append to output list.
        if l1[i1] == l2[i2]:
            output.append(l1[i1])
        # If current elements are not equal, then either the current element
        # in list one is before the current element in list two, or the other
        # way around.
        # If list one's current element is before list two's current element,
        # advance to next element in list two.
        elif l1[i1] < l2[i2]:
            i2 += 1
        # If list two's current element is before list one's current element,
        # advance to next element in list one.
        elif l1[i1] > l2[i2]:
            i1 += 1

    # Sort the output list and return it.
    return sorted(output)
