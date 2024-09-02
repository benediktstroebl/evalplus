

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l = list(l)
    seen = set()
    i = 0
    while i < len(l):
        n = l[i]
        while n in seen:
            i += 1
            n = l[i]
        seen.add(n)
        i += 1
    return l[i:]