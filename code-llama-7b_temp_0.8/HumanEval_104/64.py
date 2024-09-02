
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
    all_numbers_as_strings = [str(x) for x in x]
    filtered_strings = [x for x in all_numbers_as_strings if not '2' in x and not '4' in x and not '6' in x and not '8' in x]
    filtered_ints = [int(x) for x in filtered_strings]
    return sorted(filtered_ints)
