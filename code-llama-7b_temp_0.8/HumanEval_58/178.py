

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) < len(l2):
        short = l1
        long = l2
    else:
        short = l2
        long = l1

    # get the unique elements in short
    short_set = set(short)

    # get the unique elements in long
    long_set = set(long)

    # get the common elements
    common = short_set.intersection(long_set)

    # sort the common elements
    return sorted(common)

