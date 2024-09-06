
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
    digits_list = [int(i) for i in str(x)]
    digits_list.sort()
    odd_list = []
    for i in digits_list:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

