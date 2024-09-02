
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
        j = i
        sum = 0
        while j!= 0:
            if j % 10 % 2 == 0:
                return []
            sum += j % 10
            j = j // 10
        res.append(sum)
    res = sorted(res)
    return res
