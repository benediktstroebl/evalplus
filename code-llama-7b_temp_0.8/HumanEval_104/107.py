
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
    digits = []
    unique_digits = []

    for number in x:
        number_str = str(number)
        for digit in number_str:
            if int(digit) % 2 != 0:
                digits.append(int(digit))

    unique_digits = sorted(list(set(digits)))
    return unique_digits

