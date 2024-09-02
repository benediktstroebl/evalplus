

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    #if either list is empty
    if not l1 or not l2:
        return []

    #sort both lists
    l1.sort()
    l2.sort()

    #if the first elements are not equal
    #check the elements of the two lists until we reach the first different elements
    #or reach the end of both lists
    i = 0
    while i < len(l1) and i < len(l2) and l1[i] == l2[i]:
        i += 1

    #return the elements that are common to both lists
    return l1[:i]
