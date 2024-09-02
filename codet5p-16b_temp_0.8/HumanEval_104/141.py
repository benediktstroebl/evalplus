
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

    
    list_digits = [int(i) for i in str(x)]
    list_digits.sort()
    
    new_list = []
    for j in list_digits:
        if j % 2 == 0:
            pass
        else:
            new_list.append(j)
    
    return new_list
