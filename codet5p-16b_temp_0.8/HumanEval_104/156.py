
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

    digits = [0] * 10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in x:
        for j in str(i):
            digits[int(j)] += 1
    result = []
    for i in x:
        if digits[int(j)] == 1:
            result.append(i)
    result.sort()
    return result
