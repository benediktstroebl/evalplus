
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
    _ = [str(i) for i in x]
    tags = {str(i) for i in x}
    tags = [int(i) for i in tags if i[0] == i[-1]]
    return sorted([int(i) for i in tags if i % 2 == 0])
