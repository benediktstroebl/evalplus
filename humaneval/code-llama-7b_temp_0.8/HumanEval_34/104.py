

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if l == []:
        return []
    else:
        l1 = l[:1]
        for x in l[1:]:
            if x not in l1:
                l1.append(x)
        return unique(l1)

