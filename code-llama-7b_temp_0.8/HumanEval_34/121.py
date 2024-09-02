

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # return sorted(list(set(l)))
    # O(n log n)
    # return list(set(l))
    # O(n)
    l.sort()
    l_i = 0
    l_len = len(l)
    for i in range(1, l_len):
        if l[i] != l[l_i]:
            l_i += 1
            l[l_i] = l[i]
    return l[:l_i+1]

