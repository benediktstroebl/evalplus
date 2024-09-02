

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    for idx in range(len(l) - 1):
        if l[idx] == l[idx + 1]:
            l[idx + 1] += 1
        else:
            l[idx] += 1
    l.append(1)
    return l

