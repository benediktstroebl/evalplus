
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
    unique_list = []
    for number in x:
        unique_list.append(number)
        while len(unique_list) > 1:
            if unique_list[0] % 2 == 0:
                break
            unique_list.remove(unique_list[0])
    return unique_
