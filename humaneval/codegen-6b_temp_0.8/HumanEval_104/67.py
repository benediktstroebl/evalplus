
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
    # For each number, check if it's even. If it's even, ignore it.
    # Otherwise, add it to the result.
    # If there are no even numbers, then add the whole number to the result.
    result = []
    for x in x:
        if x % 2 == 0:
            continue
        else:
            result.append(x)
    return sorted(result)
