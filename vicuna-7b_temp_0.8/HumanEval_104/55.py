
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
    x = list(x)
    even_digits = []
    while x:
        digit = x.pop()
        if not any(digit in str(n) for n in x):
            even_digits.append(digit)
        elif digit in str(x[0]):
            even_digits.append(digit)
        else:
            even_digits.append(0)
    return sorted(even_digits)
