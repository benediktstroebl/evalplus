

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Every time you find a new item, append it to the result
    # and add its index to the exclusion list
    res = []
    ex = []
    for i, item in enumerate(l):
        if i in ex:
            continue
        for j, other in enumerate(l[i+1:]):
            if item == other:
                ex.append(i+j+1)
                break
        res.append(item)
    return res

