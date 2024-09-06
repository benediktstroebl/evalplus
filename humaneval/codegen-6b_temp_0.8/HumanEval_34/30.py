

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    tuples = [(x, i) for i, x in enumerate(l)]
    tuples.sort()
    # list out of tuples
    l_out = [l[1] for l in tuples]
    return l_out

