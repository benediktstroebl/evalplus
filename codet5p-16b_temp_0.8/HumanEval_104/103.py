
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

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    digits = [d for d in range(0, 10)]
    x = sorted(x)
    while len(x) > 0:
        if is_even(x[0]):
            x = x[1:]
        else:
            if x[0] in digits:
                digits.remove(x[0])
            x = x[1:]
    return digits
    
