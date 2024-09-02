

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    # Find unique numbers.
    for i in range(len(l)):
        while l.count(l[i]) > 1:
            l.remove(l[i])

    # Sort the unique numbers.
    l.sort()
    return l

