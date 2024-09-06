
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
        """Helper function to check if an integer x has any even digit."""
        x = str(x)
        return any(i%2==0 for i in x)
    
    res = []
    for y in x:
        if not is_even(y):
            res.append(y)
    res.sort()
    return res
