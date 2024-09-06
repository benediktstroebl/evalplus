
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
    # convert x to set
    x_set = set(x)
    # filter out even numbers
    odd_list = [x for x in x_set if not x % 2 == 0]
    return sorted(odd_list)
