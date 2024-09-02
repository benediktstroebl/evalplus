
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
    # initialize the result
    result = []
    # initialize the min and max digit value
    min_val = x[0]
    max_val = x[0]
    for i in x:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    # divide the result into chunks of length min_val
    # use list slicing
    for i in range(min_val, max_val + 1):
        result.append(list(filter(lambda x: x % 2 != 0, x)))
    return sorted(result)

