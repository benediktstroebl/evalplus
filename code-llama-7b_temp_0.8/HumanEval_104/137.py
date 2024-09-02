
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
    # 
    def unique_helper(x, y):
        x_str = str(x)
        for i in range(len(x_str)):
            if x_str[i] in y:
                continue
            else:
                return False
        return True

    unique_digits = []
    for i in range(len(x)):
        if unique_helper(x[i], unique_digits):
            unique_digits.append(x[i])

    unique_digits.sort()
    return unique_digits
