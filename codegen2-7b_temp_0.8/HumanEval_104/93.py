
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
    n = len(x)
    if n < 1:
        return []
    if n == 1:
        return [x[0]]
    else:
        even = []
        for i in range(n):
            if x[i] % 2 == 0:
                even.append(x[i])
        return unique_digits(even
