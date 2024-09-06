

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    i = 0
    while i < len(l):
        if i + 1 >= len(l):
            return sorted(l)
        j = i + 1
        while j < len(l):
            if l[i] == l[j]:
                l.pop(j)
            else:
                j += 1
        i += 1
    return sorted(l)
