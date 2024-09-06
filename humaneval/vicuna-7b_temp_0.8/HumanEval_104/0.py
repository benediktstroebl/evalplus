
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
    x = sorted(x)
    s = []
    for num in x:
        for i in range(len(str(num))):
            if not str(num)[i] in ['0', '2', '4', '6', '8']:
                s.append(num)
                break
    return s
