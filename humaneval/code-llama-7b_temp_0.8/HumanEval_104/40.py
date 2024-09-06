
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
    seen_digits = set()
    seen_digits_in_numbers = set()
    result = []
    for x_i in x:
        x_i_string = str(x_i)
        seen_digits.clear()
        for char in x_i_string:
            if char in seen_digits:
                break
            else:
                seen_digits.add(char)
        else:
            result.append(x_i)
    return sorted(result)

