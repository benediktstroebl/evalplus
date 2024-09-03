def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    l1 = deepcopy(l)
    while len(l1) > 0:
        if len(l1) == 1:
            yield l1[0]
            del l1[0]
            continue
        l2 = l1[:1]
        while len(l2) > 0:
            yield l2[-1] + 1
            del l2[-1]
        l1.pop()
        yield 1

