

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Necessary to add empty list as first element of sorted lists
    # for Python 3.10
    l1 = [[]] + sorted(l1)
    l2 = [[]] + sorted(l2)

    # Traverse both arrays from left to right
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):
        # If current element in first array is smaller
        # than current element in second array
        if l1[i] <= l2[j]:
            i += 1
        # If current element in first array is greater
        # than current element in second array
        elif l1[i] > l2[j]:
            j += 1
        # If current elements in both arrays are same
        else:
            res.append(l1[i])
            i += 1
            j += 1
    return res

