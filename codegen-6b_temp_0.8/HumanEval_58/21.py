

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # To get started, your code should only have to handle three cases:
    # if l1 is empty, l2 is empty, or if l1 and l2 have a different length.
    # Hint: you can assume that l1 and l2 are lists of integers.
    if not l1 or not l2:
        return []
    if len(l1) != len(l2):
        return []
    # If l1 is a list of integers and l2 is a list of integers,
    # then you should do this:
    # return [x for x in l1 if x in l2]
    l3 = []
    for x in l1:
        if x in l2:
            l3.append(x)
    l3.sort()
    return l3

