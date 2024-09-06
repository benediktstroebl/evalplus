

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) > len(l2):
        small, large = l2, l1
    else:
        small, large = l1, l2

    # we use a set for fast lookup
    small = set(small)
    # this will contain the common elements
    common = []
    # loop over the large list
    for item in large:
        # check if the current item is available in the set
        if item in small:
            # add it to the common list
            common.append(item)
            # remove the current item from the set
            small.remove(item)

    return common

