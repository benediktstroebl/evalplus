
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
    digits = set()
    for num in x:
        int_num = int(num)
        if any(int_num % 2 == 0 for int_num in str(num)):
            digits.add(int_num)
    return sorted(list(digits))

