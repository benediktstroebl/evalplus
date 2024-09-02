

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Algorithm from: http://code.activestate.com/recipes/111499-ginys-guerchard-unique-value-sorted-set/
    return sorted(list(set(l)))
