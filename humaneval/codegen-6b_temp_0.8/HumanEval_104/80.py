
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
    
    # insert your code here
    # convert x to a list
    x_list = list(x)
    # print(x_list)
    # go through each item
    for i in range(len(x_list)):
        # print(i)
        # print(type(x_list[i]))
        # check each element
        # if a digit is even, remove it
        if int(x_list[i]) % 2 == 0:
            x_list.remove(x_list[i])
    # print(x_list)
    return sorted(x_list)   

    