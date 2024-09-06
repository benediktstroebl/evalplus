
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
    
    unique = []
    for i in x:
        num = i % 10
        if i % 2 == 0:
            if num in unique:
                continue
            else:
                unique.append(num)
        else:
            continue
    return sorted(unique)
