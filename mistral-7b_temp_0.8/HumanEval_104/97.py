
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
    # This is a recursive solution.
    
    def is_odd(x):
        return x%2 != 0
    
    # The recursion here is to make sure the return value is sorted in
    # increasing order.
    
    if len(x) == 0:
        return []
    if is_odd(x[0]):
        return x[0] + unique_digits(x[1:])
    else:
        return unique_digits(x[1:])
    
    
    return sorted(unique_digits(x))
    























































































































