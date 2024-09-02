
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
    
    unique_digits = []

    for element in x:
        if any(digit % 2 == 0 for digit in str(element)):
            pass
        else:
            unique_digits.append(element)
    
    return unique_digits
