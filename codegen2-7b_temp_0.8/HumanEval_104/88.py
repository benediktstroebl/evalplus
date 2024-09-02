
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
    count = 0
    even_count = 0
    for num in x:
        count += 1
        if num % 2 == 0:
            even_count += 1
        if even_count == 2:
            break
    return sorted(x[count:]
