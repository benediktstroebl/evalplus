

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # if l[-1] < 9:
    #     l[-1] += 1
    # else:
    #     for i in range(len(l)-1, -1, -1):
    #         if l[i] < 9:
    #             l[i] += 1
    #             return l
    return l + [x+1 for x in l[::-1]]

