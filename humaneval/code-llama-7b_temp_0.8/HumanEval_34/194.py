

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l2 = [l[0]]
    for x in l[1:]:
        if x != l2[-1]:
            l2.append(x)
    return l2

