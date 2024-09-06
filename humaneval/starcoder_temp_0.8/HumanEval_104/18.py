
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

    # Filter elements in the list that have an even digit.
    even_digits = filter(lambda x: any([int(i) % 2 == 0 for i in str(x)]), x)

    # Return the unique digits in the list.
    return sorted(set(x) - set(even_digits))

