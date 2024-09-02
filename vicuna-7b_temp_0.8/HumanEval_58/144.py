

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

    # get the sorted lists of unique elements
    unique1 = [element for element in l1 if element not in l2]
    unique2 = [element for element in l2 if element not in l1]

    # get the intersection of unique1 and unique2
    intersection = [element for element in unique1 if element in unique2]

    # return the sorted unique common elements
    return intersection