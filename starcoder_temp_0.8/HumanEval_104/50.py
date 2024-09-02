
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
    lst = []
    for i in x:
        lst.append(i)
    new = []
    for i in range(0,len(lst)):
        if len(str(lst[i]))%2==0:
            new.append(lst[i])
    new = sorted(new)
    return new
