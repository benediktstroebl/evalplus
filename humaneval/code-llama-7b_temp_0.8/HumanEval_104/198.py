
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
    # Your code here
    if x==[]:
        return x
    even=False
    for i in x:
        if(i%2==0):
            even=True
    if even==False:
        x.sort()
        return x
    else:
        return []
