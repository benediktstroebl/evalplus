

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # make a set for O(1) lookup
    uniq = set(l)
    # convert back to a list to meet the specs
    return sorted(list(uniq))
