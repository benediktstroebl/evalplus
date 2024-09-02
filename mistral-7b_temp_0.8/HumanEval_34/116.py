

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Note: the 'is' operator will not check for the values only, it will check for the whole object
    # ref: https://stackoverflow.com/questions/2886386/how-to-check-if-two-lists-contain-the-same-elements
    res = []
    for elem in l:
        if not elem in res:
            res.append(elem)
    return sorted(res)

