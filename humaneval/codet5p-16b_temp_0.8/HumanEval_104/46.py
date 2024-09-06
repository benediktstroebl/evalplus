
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

    numbers = []
    for x in x:
        if any(num % 2 == 0 for num in str(x)):
            pass
        else:
            numbers.append(x)
    return sorted(numbers)

