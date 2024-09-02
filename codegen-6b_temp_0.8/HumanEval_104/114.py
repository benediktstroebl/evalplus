
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
    unique_number_list = []
    for number in x:
        if all(int(i) % 2 == 0 for i in str(number)):
            continue
        else:
            unique_number_list.append(number)
    return sorted(unique_number_list)

unique_digit = unique_digits([15, 33, 1422, 1])