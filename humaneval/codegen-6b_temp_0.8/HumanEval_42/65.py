

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # create new list
    # loop through l
    # set i to index of current element (i = 0 initially)
    # set n to index of next element (n = i + 1 initially)
    # while n is less than length of l
        # set i to n
        # set n to n + 1 (needs to increment n as well)
        # increment l[i] by 1
    # return l
    new_list = []
    for elem in l:
        new_list.append(elem + 1)
    return new_list

