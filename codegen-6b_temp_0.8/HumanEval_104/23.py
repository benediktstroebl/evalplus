
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
    """
    Because the first digit is always even and increase by 2 each time, 
    we could use that condition (and the first for loop) to scan the 
    input list and return all numbers that doesn't have any even number.
    """
    return sorted(list(set(x)))

