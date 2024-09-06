
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
    def is_odd(y):
        return y % 2 == 1

    def odd_digit(x):
        x_str = str(x)
        return not any(is_odd(int(s)) for s in x_str)

    return list(filter(odd_digit, x))
