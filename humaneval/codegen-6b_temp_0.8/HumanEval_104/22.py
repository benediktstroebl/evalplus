
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
    uniq_nums = []
    for num in x:
        if num < 10:
            if num % 2 != 0:
                uniq_nums.append(num)
        else:
            y = str(num)
            if y[1] != y[2]:
                uniq_nums.append(num)
    return sorted(uniq_nums)
