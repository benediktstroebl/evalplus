

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # first, sort the list
    l.sort()
    # next, iterate through the list and create a set
    # with all elements
    l = set(l)
    # finally return the sorted elements in the set
    return sorted(list(l))
