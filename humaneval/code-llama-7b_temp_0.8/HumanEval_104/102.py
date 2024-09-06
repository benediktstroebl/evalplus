
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
    new_list = []
    for num in x:
        str_num = str(num)
        all_unique = True
        for digit in str_num:
            if int(digit) % 2 == 0:
                all_unique = False
        if all_unique:
            new_list.append(num)
    return sorted(new_list)


