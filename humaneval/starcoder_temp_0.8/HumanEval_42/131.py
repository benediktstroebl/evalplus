

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # return [x + 1 for x in l]

    """
    The above list comprehension is the same as the following for loop:

    i = 0
    new_list = []
    while i < len(l):
        new_list.append(l[i] + 1)
        i = i + 1
    return new_list
    """

