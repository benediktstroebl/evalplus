
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
    if not x:
        return []

    # Remove even digits
    for number in x:
        while number % 2 == 0:
            number /= 10
            x.remove(number)

    # Sort the list in increasing order
    x.sort()

    return x

