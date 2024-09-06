
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
    d_sum = sum(x)
    even_digits = []
    for i in x:
        if d_sum % i == 0:
            continue
        else:
            even_digits.append(i)
    return sorted(even_digits)
    
