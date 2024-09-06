
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

    new_x = []
    for i in x:
        str_x = str(i)
        odd_digit = 0
        for digit in str_x:
            if int(digit) % 2 == 1:
                odd_digit += 1
        if odd_digit == len(str_x):
            new_x.append(i)
    return sorted(new_x)




