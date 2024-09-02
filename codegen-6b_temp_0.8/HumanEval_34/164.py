

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l.sort()
    assert all(isinstance(i, type(l[0])) for i in l)
    return [l[0]] + [i for i in l if i != l[0]]
