
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
    digits = [int(i) for i in str(x)]
    num_of_even_digits = sum(filter(lambda x: x % 2 == 0, digits))
    if num_of_even_digits % 2 == 0:
        return []
    else:
        return sorted(digits)
