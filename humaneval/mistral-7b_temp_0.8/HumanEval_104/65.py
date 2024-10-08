
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
    result = []
    for num in x:
        digits = str(num)
        for i in range(len(digits)):
            if digits[i] % 2 == 0:
                result.append(False)
                break
        else:
            result.append(True)
    return [num for num in x if result[x.index(num)]]
