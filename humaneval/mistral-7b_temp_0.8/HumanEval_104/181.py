
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
    x = list(map(int, x))
    result = []
    for num in x:
        if num == 0 or (num != 0 and all(d % 2 != 0 for d in str(num))):
            result.append(num)
    return sorted(result)

