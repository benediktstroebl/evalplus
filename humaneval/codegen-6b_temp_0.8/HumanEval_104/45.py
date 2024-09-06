
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
    duplicates = list(set([dig for dig in x if x.count(dig) > 1]))
    no_duplicates = [dig for dig in x if dig not in duplicates]
    return sorted(no_duplicates)

