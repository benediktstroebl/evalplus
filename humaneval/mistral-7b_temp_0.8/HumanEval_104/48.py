
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
    return_list = []
    for i in x:
        if i % 2 == 0:
            if i % 5 == 0:
                if i % 7 == 0:
                    return_list.append(i)
        else:
            return_list.append(i)
    return_list.sort()
    return return_list
