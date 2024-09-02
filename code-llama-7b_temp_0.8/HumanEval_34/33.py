

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # init a new list, add unique elements to it
    ret = []
    for i in l:
        if i not in ret:
            ret.append(i)
    # sort the list
    ret.sort()
    return ret
