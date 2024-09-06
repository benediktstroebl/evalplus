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
    odd_digits = []
    for num in x:
        num_str = str(num)
        if not any(char.isdigit() and char % 2 == 0 for char in num_str):
            odd_digits.append(int(num))
    return sorted(odd_digits)