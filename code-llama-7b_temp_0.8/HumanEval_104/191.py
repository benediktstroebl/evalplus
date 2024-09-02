
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
    result = []
    for el in x:
        n = str(el)
        for x in n:
            if int(x) % 2 == 0:
                break
        else:
            result.append(el)
    return sorted(result)
