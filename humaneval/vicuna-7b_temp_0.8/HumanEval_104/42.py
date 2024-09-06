
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
    digit_set = set()
    for num in x:
        digit = sum(int(i) for i in str(num))
        if digit % 2 == 0:
            return []
        digit_set.add(digit)
    return sorted(digit_set)
