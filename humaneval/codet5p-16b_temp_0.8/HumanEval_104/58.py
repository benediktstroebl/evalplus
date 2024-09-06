
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
    for digit in x:
        temp = digit
        while temp > 0:
            if temp % 10 % 2 == 0:
                break
            temp = temp // 10
        else:
            result.append(digit)
    result.sort()
    return result
    
    
