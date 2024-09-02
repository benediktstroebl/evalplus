
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
    for n in x:
        str_n = str(n)
        flag = True
        for ch in str_n:
            if int(ch) % 2 == 0:
                flag = False
                break
        if flag:
            res.append(n)
    return sorted(res)
