

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    n = len(l)
    if n == 0:
        return []

    i = 0
    j = 1

    while j < n:
        if l[i]!= l[j]:
            i += 1
            l[i] = l[j]
        j += 1

    return l[:i+1]
