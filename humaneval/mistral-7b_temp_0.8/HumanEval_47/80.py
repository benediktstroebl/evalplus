

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # use binary search to find median value of list
    # then find values in list that are <= median
    # then find values in list that are <= median

    l = sorted(l)

    # find median value
    median = l[int(len(l) / 2)]
    median_idx = int(len(l) / 2)

    num_less_or_equal = 0
    for idx, val in enumerate(l):
        if val <= median:
            num_less_or_equal += 1

    num_greater_or_equal = len(l) - num_less_or_equal

    if num_greater_or_equal == num_less_or_equal:
        return l[median_idx]
    elif num_less_or_equal > num_greater_or_equal:
        return l[median_idx - 1]
    else:
        return l[median_idx]
