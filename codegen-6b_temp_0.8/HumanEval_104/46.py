
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
    number_list = []
    for item in x:
        item_str = str(item)
        number_list.append([item_str[i] for i in range(0, len(item_str)) if item_str[i] not in ['0', '2', '4', '6', '8']])
    number_list.sort()
    return number_list

