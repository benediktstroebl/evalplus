
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # return [i for i in x if any(((str(i)[j] + str(i)[j+1]) % 2 != 0) for j in range(len(str(i)) - 1))]
    return [x for x in x if not any((x % (10 ** j) % 10 in {0, 2, 4, 6, 8}) for j in range(len(str(x))))]
