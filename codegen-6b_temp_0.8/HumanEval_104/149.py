
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
    def has_even_digit(x):
        for c in str(x):
            if c in '02468':
                return True
        return False
    
    def check_digits(x):
        for c in str(x):
            if not c in '0123456789':
                return False
        return True
    
    return sorted([x for x in x if not has_even_digit(x) and check_digits(x)])
