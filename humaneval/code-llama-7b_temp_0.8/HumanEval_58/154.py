

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # get the smaller list
    if len(l1) < len(l2):
        l3 = l1
        l4 = l2
    else:
        l3 = l2
        l4 = l1

    # sort the smaller list
    l3.sort()

    # iterate through smaller list
    for i in l3:
        if l4.count(i) > 0:
            print(i, end=" ")

