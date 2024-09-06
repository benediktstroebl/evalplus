
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
    for element in x:
        even_digit = []
        for digit in str(element):
            if int(digit) % 2 == 0:
                even_digit.append(digit)
        if not even_digit:
            new_list.append(element)
    return sorted(new_list)
