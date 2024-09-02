
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

    digit_list = []
    for i in x:
        x_digit = 0
        while i > 0:
            x_digit = i%10
            if x_digit % 2 == 0:
                break
            i = i//10
        else:
            digit_list.append(x_digit)
    return sorted(digit_list)

