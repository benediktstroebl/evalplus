

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # TODO: Implement me!
    # Hint: You may use list.sort() and list.pop()
    l.sort()
    res = []
    for i in range(len(l)):
        if i == 0 or l[i] != l[i - 1]:
            res.append(l[i])
    return res

