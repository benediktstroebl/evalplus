

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Use set to ignore duplicates and sort them
    # Use set for O(1) complexity to check if element is in set
    # use list for O(n) complexity to get elements from list
    set1 = set(l1)
    set2 = set(l2)
    common = []
    # for each element in set2 check if element is in set1
    for i in set2:
        if i in set1:
            common.append(i)
    common.sort()
    return common

