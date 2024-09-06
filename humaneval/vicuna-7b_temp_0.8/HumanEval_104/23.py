
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
    digits = sum(1 for num in x for num // 2 in range(len(str(num))))
    return [num for num in x if not any(str(num).isdigit(i) for i in range(len(str(num))))]
