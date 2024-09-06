
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
    # return set([int(digit) for digit in str(x) if int(digit) % 2 == 1])
    # return sorted(set(int(digit) for digit in str(x) if int(digit) % 2 == 1))
    # return sorted(set(int(digit) for digit in str(x) if int(digit) % 2 != 0))
    # return sorted(int(digit) for digit in str(x) if int(digit) % 2 != 0)
    return sorted(int(digit) for digit in str(x) if int(digit) % 2 != 0)


