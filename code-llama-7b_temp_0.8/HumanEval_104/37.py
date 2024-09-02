
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
    unique_digits = set()
    for x in nums:
        num_string = str(x)
        num_string_set = set(num_string)
        num_string_set = num_string_set - {str(i) for i in range(2,10,2)}
        num_string = ''.join(num_string_set)
        unique_digits.add(int(num_string))
    return sorted(unique_digits)
