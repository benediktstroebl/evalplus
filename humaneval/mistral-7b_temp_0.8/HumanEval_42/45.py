

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # base case: a list with 1 element.
    if len(l) == 1:
        return [l[0] + 1]
    # recursive case: a list with more than 1 element.
    else:
        # increment last element
        l[-1] += 1
        # recursively call function on the remaining list.
        return incr_list(l[:-1])

