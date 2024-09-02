
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
    
    i = 0
    even = []
    while i < len(x):
        if x[i] % 2 == 0:
            even.append(x[i])
        i += 1
    even = sorted(even)
    i = 0
    while i < len(x):
        if x[i] % 2!= 0:
            x[i] = even.pop()
        i += 1
    return
