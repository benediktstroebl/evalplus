

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    n1 = len(l1)
    n2 = len(l2)

    if n1 == 0 or n2 == 0:
        return []

    if n1 < n2:
        l1, l2 = l2, l1

    if l1[n1-1] == l2[n2-1]:
        return l1[:n1-1]

    # Sort both lists to simplify checking
    l1.sort()
    l2.sort()

    # Find the first difference
    i1 = 0
    while i1 < n1 and l1[i1] == l2[0]:
        i1 += 1

    # Check the rest of the first list
    j1 = i1
    while j1 < n1 and l1[j1] == l2[1]:
        j1 += 1

    if j1 == n1:
        return []

    # Find the first common element
    i2 = j1
    while i2 < n2 and l2[i2] == l1[j1]:
        i2 += 1

    # Return the first common element
    return l1[j1:i1+1]