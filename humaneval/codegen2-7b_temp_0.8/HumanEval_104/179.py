
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
    if len(x) < 2:
        return x
    
    x_even = [x[i] for i in range(len(x)) if x[i] % 2 == 0]
    x_odd = [x[i] for i in range(len(x)) if x[i] % 2!= 0]
    
    return sorted(x_even + unique_digits(x_odd))
    
