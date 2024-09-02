

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # sort both lists
    l1.sort()
    l2.sort()

    # create a set of unique elements from the first list
    unique_l1 = set(l1)

    # get the elements that are in the second list but not in the first set
    l3 = [x for x in l2 if x not in unique_l1]

    # get the elements that are in the first set but not in the second list
    l4 = [x for x in l1 if x not in l2]

    # return the sorted unique elements in l3 and l4 combined
    return sorted(l3 + l4)