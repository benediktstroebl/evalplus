
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
    # Don't change this line!
    # Write your code below
    x.sort()
    l1 = []
    l2 = []
    for i in x:
        if i%2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l2.sort()
    y = l1 + l2
    return y
