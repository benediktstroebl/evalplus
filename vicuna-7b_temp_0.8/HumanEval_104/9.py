
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
    for i in range(1, len(x)):
        if not any(str(n) % 2 == 0 for n in x[i:]):
            result.append(x[i])
            x = x[:i] + x[i+1:]
    return result
