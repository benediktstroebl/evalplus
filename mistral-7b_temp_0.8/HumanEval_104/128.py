
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
    # YOUR CODE HERE

    result = []

    for item in x:
        if all(i%2 == 0 for i in list(str(item))):
            continue
        else:
            result.append(item)
    result = sorted(result)

    return result

