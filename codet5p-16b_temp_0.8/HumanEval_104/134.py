
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
    for i in x:
        num = i
        while num > 0:
            if num % 10 % 2 == 0:
                break
            num = num // 10
        else:
            res.append(i)
    return sorted(res)

