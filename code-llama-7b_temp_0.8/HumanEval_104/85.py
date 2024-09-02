
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

    # return [x for x in xs if not 2 <= x <= 99 % 2]
    # return [x for x in xs if (x - 1) % 2 + 1 != x]
    # return [x for x in xs if x != 2 * x // 2]
    return [x for x in xs if not any(map(lambda x: x in '02468', str(x)))]

