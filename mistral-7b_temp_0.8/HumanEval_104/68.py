
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
    for number in x:
        new_digit = number
        number_digits = []
        while new_digit > 0:
            new_digit, digit = divmod(new_digit, 10)
            number_digits.append(digit)
        number_digits = sorted(list(set(number_digits)))
        if number not in new_list and all(map(lambda i: i%2 == 0, number_digits)):
            new_list.append(number)
    return sorted(new_list)
