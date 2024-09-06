

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    # Order preserving
    # s = set()
    # for x in l:
    #     if x not in s:
    #         s.add(x)
    # return sorted(s)

    # Not order preserving
    return list(set(l))
