
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
    digits = [int(i) for i in str(x)]
    result = []
    for i in range(len(digits)):
        if not any(digit == 2 for digit in digits[i+1:]):
            result.append(digits[i])
    return sorted(result)
