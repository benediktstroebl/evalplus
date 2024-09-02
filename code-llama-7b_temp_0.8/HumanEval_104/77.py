
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

    filtered_list = []

    for i in x:
        if "2" not in str(i) and "4" not in str(i) and "6" not in str(i) and "8" not in str(i):
            filtered_list.append(i)

    return sorted(filtered_list)

