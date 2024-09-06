
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
    digit = 0
    digits = []
    while x:
        if x % 2 == 0:
            break
        digit += 1
    for num in x:
        digits.append(digit % 10)
        digit /= 10
    return digits
