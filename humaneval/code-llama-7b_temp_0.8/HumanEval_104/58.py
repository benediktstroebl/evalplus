
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
    list_all = []
    for num in x:
        num_copy = num
        list_duplicate = []
        while num_copy > 0:
            last_digit = num_copy % 10
            num_copy = num_copy // 10
            if last_digit % 2 != 0:
                list_duplicate.append(last_digit)
            else:
                continue
        list_all.append(list_duplicate)
    list_all.sort()
    return list_all
