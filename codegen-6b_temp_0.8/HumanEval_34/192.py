

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    assert isinstance(l, list), "a list is required"
    l = l[:]
    l.sort()
    last = l[0]
    l_set = [last]
    for i in l[1:]:
        if i != last:
            l_set.append(i)
            last = i
    return l_set

