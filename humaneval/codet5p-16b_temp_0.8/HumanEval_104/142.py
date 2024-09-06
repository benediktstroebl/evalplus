
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

    list_no_even = []
    for number in x:
        if number % 2!= 0:
            list_no_even.append(number)
            list_no_even.sort()
            
    return list_no_even
    
