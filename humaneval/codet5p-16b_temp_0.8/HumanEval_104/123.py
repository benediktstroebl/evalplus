
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

    
    num_list = []
    for i in x:
        odd_digits = []
        for digit in str(i):
            if int(digit) % 2!= 0:
                odd_digits.append(digit)
        if len(odd_digits) == 1:
            num_list.append(i)
    return sorted(num_list)

