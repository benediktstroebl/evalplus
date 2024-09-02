
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
    unique_digits_list = []
    for num in x:
        if all(num % 2 != 0 for num in str(num)):
            unique_digits_list.append(num)
        else:
            continue
    return unique_digits_list
