
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
    
    def has_even_digits(y):
        if y < 10 and y % 2 == 0:
            return True
        elif y < 10:
            return False
        else:
            return has_even_digits(y // 10) or y % 10 % 2 == 0

    return sorted([i for i in x if not has_even_digits(i)])
