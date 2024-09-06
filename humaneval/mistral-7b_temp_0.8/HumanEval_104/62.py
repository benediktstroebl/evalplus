
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

    odd_elements = []
    for i in x:
        number = str(i)
        odd_digits = [digit for digit in number if int(digit) % 2 != 0]
        odd_elements.append(i)
    odd_elements.sort()
    return odd_elements
