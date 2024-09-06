

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    n = len(l)
    if n == 0:
        return []
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] == l[j]:
                l.remove(l[i])
                break
    return l
