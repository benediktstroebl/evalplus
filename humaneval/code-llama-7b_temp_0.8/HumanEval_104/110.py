
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
    list_in = [str(i) for i in x]
    list_out = []
    for i in list_in:
        if all(int(j) % 2 != 0 for j in i):
            list_out.append(int(i))
    list_out.sort()
    return list_out
