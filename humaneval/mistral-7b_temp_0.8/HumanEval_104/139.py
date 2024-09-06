
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
    out = []
    for el in x:
        tmp = []
        for num in str(el):
            if int(num)%2==0:
                tmp.append(1)
            else:
                tmp.append(0)
        if tmp.count(0)==len(tmp):
            out.append(el)
    return sorted(out)
