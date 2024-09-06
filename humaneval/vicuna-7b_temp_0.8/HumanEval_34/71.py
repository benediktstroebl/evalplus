

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if not l:
        return []
    n = len(l)
    d = [None]*n
    i = 0
    while i < n:
        while i < n and l[i] == l[i+1]:
            i += 1
        if l[i] is None:
            d[i] = l[i]
            i += 1
        else:
            d[i] = l[i]
            i += 1
    return [d[j] for j in range(n)]
