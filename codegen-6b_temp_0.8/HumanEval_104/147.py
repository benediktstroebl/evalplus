
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
    result_list = []
    for number in x:
        str_number = str(number)
        is_even = False
        for digit in str_number:
            if int(digit) % 2 == 0:
                is_even = True
                break
        if is_even == False:
            result_list.append(number)
    return sorted(result_list)
