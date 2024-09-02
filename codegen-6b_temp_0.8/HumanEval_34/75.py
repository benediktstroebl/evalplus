

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # similar to set(s) but preserving order
    l = iter(l) # iterate through l
    uniques = [next(l)] # get first element
    for x in l: # break when there is a new unique element
        if x != uniques[-1]:
            uniques.append(x)
    return uniques
