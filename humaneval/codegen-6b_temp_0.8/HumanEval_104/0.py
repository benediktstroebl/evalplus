
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
    # list of all digits
    num_list = []
    # for each number in x
    for num in x:
        # for each digit
        for digit in str(num):
            # add it to the list if it's not there yet
            if int(digit) not in num_list:
                num_list.append(int(digit))
    # sort the list
    num_list.sort()
    # return the list
    return num_list

