

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    # convert to set to eliminate duplicates
    # convert back to list as lists are easier to reason about in 
    # comparison to sets
    return sorted(list(set(l)))

