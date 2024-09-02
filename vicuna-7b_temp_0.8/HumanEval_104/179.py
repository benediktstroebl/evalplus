
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
    x = list(x)
    while x:
        if not any(x % 2 == 0 for x in x):
            y = x[:]
            while y:
                if not any(y % 2 == 0 for y in y):
                    y = y[1:]
                    if y:
                        x.append(y[0])
                        break
                    else:
                        x.append(y)
                else:
                    x.append(y)
        else:
            x = x[1:]
    return x
