
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
    unique_list = []
    for i in x:
        unique = True
        while i > 0:
            if i % 10 % 2 == 0:
                unique = False
                break
            i = i // 10
        if unique:
            unique_list.append(i)
    return sorted(unique_list)

