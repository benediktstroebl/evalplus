
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

    x.sort()
    result = []
    for i in x:
        if sum(int(n) % 2 for n in str(i)) == 0:
            continue
        else:
            result.append(i)
    return result






    
