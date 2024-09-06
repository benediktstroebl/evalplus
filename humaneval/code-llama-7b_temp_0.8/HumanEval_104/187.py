
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
    for n in x:
        flag = True
        for c in str(n):
            if int(c) % 2 == 0:
                flag = False
                break
        if flag:
            result.append(n)
    return sorted(result)

