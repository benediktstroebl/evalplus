
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
    res = []
    for x in x:
        if len(str(x)) == 1:
            res.append(x)
        else:
            flag = 0
            for y in str(x):
                if int(y) % 2 == 0:
                    flag = 1
            if flag == 0:
                res.append(x)
    res.sort()
    return res

