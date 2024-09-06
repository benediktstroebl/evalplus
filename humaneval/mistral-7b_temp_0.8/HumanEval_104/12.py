
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
    even_digit = []
    for n in x:
        digits = list(str(n))
        for i in digits:
            if int(i)%2 == 0:
                even_digit.append(int(i))
    if even_digit == []:
        return x
    else:
        return unique_digits([i for i in x if not i in even_digit])
