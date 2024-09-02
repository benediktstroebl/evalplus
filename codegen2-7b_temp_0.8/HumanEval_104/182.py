
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
    if len(x) == 0:
        return x
    elif len(x) == 1:
        return x
    else:
        x2 = list(x)
        
        for i in range(len(x2)):
            if x2[i] % 2 == 0:
                continue
            else:
                x2.remove(x2[i])
                
        return x2 + sorted(x
