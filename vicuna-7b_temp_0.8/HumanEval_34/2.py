

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = {}
    seen_c = {}
    for x in l:
        x = (x,)
        while x:
            i, y = x[0], x[1]
            if i not in seen:
                seen[i] = True
                seen_c[i] = True
                x = x[2:]
            else:
                seen_c[i] = True
                x = x[2:]
        if seen_c:
            for i, j in seen_c.items():
                l.remove(j)
    return l
