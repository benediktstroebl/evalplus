
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
    output = []
    for item in x:
        num = str(item)
        digit = []
        for char in num:
            if int(char) % 2 == 0:
                digit.append(int(char))
        if len(digit) == 0:
            output.append(item)
    return output

