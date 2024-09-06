
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
    if not x:
        return []
    digits = [int(d) for d in str(x)]
    return sorted(set(digits) - set([sum(int(d) ** i * i for i in range(2, len(digits) + 1)) for d in digits if int(d) > 0]))
