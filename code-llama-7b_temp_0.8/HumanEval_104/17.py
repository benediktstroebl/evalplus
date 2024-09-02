
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
    evens_in_x = [i for i in x if not '2' in str(i)]
    odds_in_x = [i for i in evens_in_x if not '0' in str(i)]
    return sorted(odds_in_x)

