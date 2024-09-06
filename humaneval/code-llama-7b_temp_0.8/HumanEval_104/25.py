
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
    d={}
    for i in x:
        j=0
        while i:
            if i%10 not in d.keys():
                d[i%10]=1
            i//=10
        if len(d)==10:
            return []
    for i in d.keys():
        if i%2==0:
            return []
    return sorted(d.keys())
    
    
