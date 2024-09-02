
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

    # check if input is valid
    if not isinstance(x, list):
        raise TypeError("Input argument should be a list of integers")
    if len(x) != len(set(x)):
        raise ValueError("All elements of input list should be distinct")
    if any(not isinstance(i, int) or i < 0 for i in x):
        raise ValueError("All elements of input list should be positive integers")
    if any(str(i)[0] == "0" for i in x):
        raise ValueError("All elements of input list should not have leading zeroes")
    return sorted([i for i in x if not any(str(j).isdigit() and int(str(j)[0]) % 2 == 0 for j in str(i))])
