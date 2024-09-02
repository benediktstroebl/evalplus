
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
    # Use slicing to remove all the even digits in the list
    # Use built-in functions `all` and `map` to check if all elements
    #   in the list are odd
    return sorted([n for n in x if all(map(lambda d: int(d) % 2, str(n)))])

