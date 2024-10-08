
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
    x = sorted(x)
    result = []
    for i in range(len(x)):
        while x[i] % 2 == 0:
            x[i], x[i] = x[i] // 2, x[i] * 2
            i -= 1
        result.append(x[i])
    return result
