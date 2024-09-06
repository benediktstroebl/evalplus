
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
    digits = [int(d) for d in str(x)]
    even_digits = [d for d in digits if d % 2 == 0]
    return sorted(digits, key=lambda x: x if x not in even_digits else x - (x // 2))
