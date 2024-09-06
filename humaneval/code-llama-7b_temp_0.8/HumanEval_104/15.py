
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
    even_digits = ["2", "4", "6", "8"]
    result = []
    for x_element in x:
        x_str = str(x_element)
        if all(even_digit not in x_str for even_digit in even_digits):
            result.append(x_element)
    return result

