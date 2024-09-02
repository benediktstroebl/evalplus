
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
    if x == []:
        return []
    temp = []
    for i in x:
        if i == 0:
            continue
        s = str(i)
        if int(s[len(s)-1])%2==0:
            temp.append(i)
    return sorted(temp)
