

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # base case: an empty list
    if len(l) == 0:
        return l
    # recursive case:
    # head of list + 1 + the rest of the list
    else:
        return [l[0] + 1] + incr_list(l[1:])
