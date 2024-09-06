
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
    # Append to every string in x the reversed digits in x.
    def append_digits(x, digits):
        # Complete this function.
        for i in xrange(len(x)):
            x[i] += digits[-1]
            digits = digits[:-1]
        return x
    
    # Initialize a list to be returned with the digits of x in decreasing 
    # order.
    digits = []
    # Do nothing if x is empty
    if x == []:
        return []
    # Initialize the reversed digits string as a copy of x.
    digits = x[:]
    # Make sure that x is iterable.
    if not hasattr(x, '__iter__'):
        return []
    # Remove the last digit from each element of x.
    for i in xrange(len(x)):
        digits[i] = str(digits[i])[:-1]
    # Sort the list
    digits = sorted(digits)
    # Append the digits to the result until all digits are reversed.
    while digits[-1] != 0:
        digits = append_digits(digits, digits[-1])
    return digits
