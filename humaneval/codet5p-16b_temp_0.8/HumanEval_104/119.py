
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

    sorted_list = sorted(x)
    new_list = []
    for element in sorted_list:
        temp = str(element)
        for digit in temp:
            if int(digit) % 2 == 0:
                break
            else:
                continue
        else:
            new_list.append(element)
    return new_list
