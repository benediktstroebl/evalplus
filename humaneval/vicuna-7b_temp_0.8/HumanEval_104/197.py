
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
    digit_list = [int(d) for d in str(x)]
    sorted_digit_list = sorted(digit_list)
    unique_digit_list = [d for d in digit_list if not any(int(d) % 2 == 0 for d in digit_list)]
    return sorted_digit_list[0:len(unique_digit_list)]
