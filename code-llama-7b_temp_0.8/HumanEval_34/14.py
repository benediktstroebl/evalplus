

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # fast return for empty and singleton lists
    if l == []:
        return []
    if len(l) == 1:
        return l
    # initialize the output list and the iterator on input list
    out = [l[0]]
    i = iter(l)
    # loop invariant: out and i are initialized and i is an iterator on l
    # initialize first iterator with second element of input list
    next(i, None)
    for v in i:
        if v != out[-1]:
            out.append(v)
    return out

