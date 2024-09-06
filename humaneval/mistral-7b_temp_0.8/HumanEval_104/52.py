
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
    # Check x
    if not isinstance(x, list):
        raise TypeError("x must be a list")
    for item in x:
        if not isinstance(item, int):
            raise TypeError("x must be a list of positive integers")
    # Check for empty list
    if len(x) == 0:
        raise ValueError("x must not be empty")

    # The list to return
    result = []
    # Sort the elements
    x.sort()
    # Loop through x
    for item in x:
        # The item has no even digits
        if all(digit % 2 for digit in str(item)):
            result.append(item)

    return sorted(result)

