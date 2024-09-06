
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
    return_list = []

    for number in x:
        flag = 1
        for char in str(number):
            if int(char) % 2 == 0:
                flag = 0
        if flag == 1:
            return_list.append(number)

    return return_list



