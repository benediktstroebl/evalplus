
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
    # IDEA:
    # Create a set to keep track of the elements that meet the criteria.
    # Iterate over the elements and add them to the set if they don't have any even digits.
    # Sort the set and return the sorted list.
    even_digits = set()
    for i in x:
        if even_digits(i):
            even_digits.add(i)
    return list(even_digits)


