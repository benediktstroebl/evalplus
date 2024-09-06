
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

    # your code here
    def has_no_even_digit(x):
        for char in str(x):
            if int(char) % 2 == 0:
                return False
        return True
    return list(filter(has_no_even_digit, x))
