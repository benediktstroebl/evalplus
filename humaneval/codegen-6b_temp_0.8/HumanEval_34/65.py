

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # set() returns a new set object and does not modify the original
    u = set(l)
    return [v for v in sorted(u)]
