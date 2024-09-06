
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
    # Check if x is empty
    if not x:
        return []
    
    # If x is not empty, check if it has any even digits
    for i in range(len(x)):
        if x[i] % 2 == 0:
            return x[:i] + x[i+1:]

    # If x doesn't have any even digits, return it as a sorted list
    return sorted(x)
